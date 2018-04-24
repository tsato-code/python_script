import pprint
import json
import corenlp


text = "I am Alice."


corenlp_dir = "/mnt/share/ms_topic/stanford-corenlp-full-2013-06-20/"
parser = corenlp.StanfordCoreNLP(corenlp_path=corenlp_dir)


result_json = json.loads(parser.parse(text))
pprint.pprint(result_json)


"""
$ python test_corenlp.py
{'coref': [[]],
 'sentences': [{'dependencies': [['nsubj', 'Alice', 'I'],
                                 ['cop', 'Alice', 'am'],
                                 ['root', 'ROOT', 'Alice']],
                'indexeddependencies': [['nsubj', 'Alice-3', 'I-1'],
                                        ['cop', 'Alice-3', 'am-2'],
                                        ['root', 'ROOT-0', 'Alice-3']],
                'parsetree': '(ROOT (S (NP (PRP I)) (VP (VBP am) (NP (NNP '
                             'Alice))) (. .)))',
                'text': 'I am Alice.',
                'words': [['I',
                           {'CharacterOffsetBegin': '0',
                            'CharacterOffsetEnd': '1',
                            'Lemma': 'I',
                            'NamedEntityTag': 'O',
                            'PartOfSpeech': 'PRP'}],
                          ['am',
                           {'CharacterOffsetBegin': '2',
                            'CharacterOffsetEnd': '4',
                            'Lemma': 'be',
                            'NamedEntityTag': 'O',
                            'PartOfSpeech': 'VBP'}],
                          ['Alice',
                           {'CharacterOffsetBegin': '5',
                            'CharacterOffsetEnd': '10',
                            'Lemma': 'Alice',
                            'NamedEntityTag': 'PERSON',
                            'PartOfSpeech': 'NNP'}],
                          ['.',
                           {'CharacterOffsetBegin': '10',
                            'CharacterOffsetEnd': '11',
                            'Lemma': '.',
                            'NamedEntityTag': 'O',
                            'PartOfSpeech': '.'}]]}]}
"""