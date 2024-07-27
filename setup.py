from setuptools import setup, find_packages

setup(
    name='selena',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        '',  # 필요한 패키지 추가
    ],
    entry_points={
        'console_scripts': [
            'selenacli=app:run',  # selenacli 명령어를 app.py의 stage 함수에 연결
        ],
    },
)