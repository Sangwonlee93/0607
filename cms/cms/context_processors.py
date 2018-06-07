def gnb_menus(request):
    menus = [
        {
            'name': '홈', 'url': '/admin/',
        },
        {
            'name': '회원',
            'sub_menus': [
                {'name': '관리자', 'url': '/admin/member/member/?permission__exact=AD'},
                {'name': '에디터', 'url': '/admin/member/member/?permission__exact=ET'},
                {'name': '일반', 'url': '/admin/member/member/?permission__exact=MB'},
            ]
        },
        {
            'name': ' 글 ',
            'sub_menus': [
                {'name': 'GENDER', 'url': '/admin/post/post/?category__name=GENDER'},
                {'name': 'SOCIAL', 'url': '/admin/post/post/?category__name=SOCIAL'},
                {'name': 'POLITICS', 'url': '/admin/post/post/?category__name=POLITICS'},
                {'name': '통계', 'url': '/admin/post/post/status/'},
            ]
        }
    ]
    return {'gnb_menus': menus}
