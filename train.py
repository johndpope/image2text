from model import StoryNet

storyNet = StoryNet(training_data_path='./iaprtc12', model_path='./models')
storyNet.train()
