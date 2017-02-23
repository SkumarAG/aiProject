
import sys
total = 1000

from fileread.TweetRead import importData
import numpy as np
from bagofwords.textToVector import bagofWords
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.utils import shuffle
import matplotlib.pyplot as plt
import itertools
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
X, y = importData()
X = X[1:]

y = y[1:]
X, y = shuffle(X, y, random_state=0)
tweets =np.array(X)

#X = np.array(X)
#vectorizer = CountVectorizer(min_df=2)
#X = vectorizer.fit_transform(X)

X = np.array(bagofWords(X))

y = np.array(map(int, list(y)))
num_examples = len(X)

ratio = .6
# training data
X_train = X[0:num_examples*ratio]
y_train = y[0:num_examples*ratio]

#test data
X_test = X[num_examples*ratio:]
y_test = y[num_examples*ratio:]

barLength = 20 
status = ""
class_names  = ["No Traffic info in Tweets","Traffic Info in Tweets"]

nn_input_dim = len(X[0])#neural netwoek input dimension
nn_output_dim = 2# true or false
neuron_number = 8    # in a layer
# Gradient descent parameters (I picked these by hand)
alpha = 0.001 # learning rate for gradient descent
reg_lambda = 0.001 # regularization strength
num_passe = 5000
def weight_init(L1,L2):
    return np.sqrt(6)/np.sqrt(L1 + L2) 

def calculate_loss(model):
    W1,  W2 = model['W1'], model['W2']
    # Forward propagation to calculate our predictions
    num_ex = len(X_train)
    z1 = X_train.dot(W1)
    a1 = np.tanh(z1)
    z2 = a1.dot(W2) 
    exp_scores = np.exp(z2)
    probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
    # Calculating the loss
    corect_logprobs = -np.log(probs[range(num_ex), y_train])
    data_loss = np.sum(corect_logprobs)
    # Add regulatization term to loss (optional)
    data_loss += reg_lambda/2 * (np.sum(np.square(W1)) + np.sum(np.square(W2)))
    return 1./num_ex * data_loss
def status(i,model):
    progress = (float(i)/num_passe)
    block = int(round(barLength*progress))
    sys.stdout.write('\r')
    text = "[{0}] Neural Network Training {1}% Completed.".format( "#"*block + "-"*(barLength-block), format(progress*100,".2f"),status)
    sys.stdout.write(text)
    sys.stdout.write ("           Current Loss %.5f." %(calculate_loss(model)))
    sys.stdout.flush()
    
    
def predict(model, x):
    W1,  W2 = model['W1'],  model['W2']
    # Forward propagation
    z1 = x.dot(W1) 
    a1 = np.tanh(z1)
    z2 = a1.dot(W2) 
    exp_scores = np.exp(z2)
    probs = exp_scores / np.sum(exp_scores, keepdims=True)
    return np.argmax(probs)

def build_model(nn_hdim, num_passes=num_passe, print_loss=False):
    #Initilization of weight
    #L1 number of input in the given layer
    #L2 number of input in the given layer
    sys.stdout.write("Initializing Neural Network")
    L1 = nn_input_dim
    L2 = neuron_number
    esp_init = weight_init(L1,L2)
    W1 = np.random.uniform(-esp_init,esp_init,[nn_input_dim,nn_hdim])
    L1 = neuron_number
    L2 = nn_output_dim
    esp_init = weight_init(L1,L2)
    W2 = np.random.uniform(-esp_init,esp_init,[nn_hdim, nn_output_dim])
    # This is what we return at the end
    model = {}
    # Gradient descent. For each batch...
    for i in xrange(0, num_passes):
        # Forward propagation
        z1 = X_train.dot(W1) 
        a1 = np.tanh(z1)
        z2 = a1.dot(W2) 
        exp_scores = np.exp(z2)
        probs = exp_scores / np.sum(exp_scores, axis=1, keepdims=True)
        num_ex = len(X_train)
        # Backpropagation
        delta3 = probs
        delta3[range(num_ex), y_train] -= 1
        dW2 = (a1.T).dot(delta3)
        delta2 = delta3.dot(W2.T) * (1 - np.power(a1, 2))# diff of tanh -- in future i will use gradient desent to calculate this
        dW1 = np.dot(X_train.T, delta2)
        # Add regularization terms (b1 and b2 don't have regularization terms)
        dW2 =dW2 + (reg_lambda * W2)
        dW1 = dW1 + (reg_lambda * W1)
        # Gradient descent parameter update
        W1 = W1 -(alpha * dW1)
        W2 = W2 -(alpha * dW2)     
        # Assign new parameters to the model
        model = { 'W1': W1, 'W2': W2}
        status(i,model)        
    return model
def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Reds):
    """
    Credit : Sklearn - http://scikit-learn.org/stable/auto_examples/model_selection/plot_confusion_matrix.html#sphx-glr-auto-examples-model-selection-plot-confusion-matrix-py    
    """
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    """
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.tight_layout()
    plt.ylabel('True label')
    plt.xlabel('Predicted label')    
## Build a model
##model = build_model(neuron_number, print_loss=True)
model = {}
model['W1'] = np.loadtxt(fname='layer1.weight',delimiter=',')
model['W2'] = np.loadtxt(fname='layer2.weight',delimiter=',')
y_pred = []
#predict(model, X_test[0])
for i in X_test:    
    y_pred.append(predict(model,i))
    
# Compute confusion matrix
cnf_matrix = confusion_matrix(y_test, y_pred)

# Plot non-normalized confusion matrix
plt.figure()
plot_confusion_matrix(cnf_matrix, classes=class_names,
                      title='Confusion matrix, without normalization')

accuracy_score(y_test, y_pred,normalize=False)

#Finding incorrect prediction

in_correct = np.not_equal(y_test,y_pred)# true where there is difference

in_correct_index = np.nonzero(in_correct)# will return the index of all true value, in turn all the incorrect value

index_tweets = np.array(in_correct_index) + len(X_train)

in_correct_tweet = tweets[[in_correct_index]]

actual_value = y_test[[in_correct_index]]

predict_value = y_pred[[in_correct_index]]

#below actual should be same as actual_value

actual_value1 = y[[index_tweets]]
