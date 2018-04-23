import pprint
import json
import corenlp


# text
text = "I am Alice."

# Stanford CoreNLPへのパス
corenlp_dir = "/mnt/share/ms_topic/stanford-corenlp-full-2013-06-20/"

# パーサの生成
parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)

# パースして結果をpretty print
result_json = json.loads(parser.parse(text))
pprint.pprint(result_json)
