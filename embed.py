from towhee import AutoPipes, AutoConfig

insert_conf = AutoConfig.load_config('eqa-insert')
insert_conf.host = '10.1.10.20'
insert_conf.port = '19530'
insert_conf.collection_name = 'test_rag'

insert_pipe = AutoPipes.pipeline('eqa-insert', config=insert_conf)
insert_pipe('./data/history24/baihuasanguozhi.txt')