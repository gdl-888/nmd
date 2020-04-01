import re

def getTime():
    return str(datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S"));

def generateTime(t, fmt = 'Y-m-d H:i:s'):
    try:
        ddd = t.split(' ')[0];
        ttt = t.split(' ')[1];
        return '<time datetime="' + ddd + 'T' + ttt + '.000Z" data-format="' + fmt + '">' + t + '</time>';
    except:
        return t;

def markdown(content):
    content = html.escape(content);
    content = re.sub('\r', '', content);

    content = re.sub('[{][{][{][#][!]wiki\s{0,}style[=]["](?P<is>(?:(?!["]).)+)["]\s{0,}\n(?P<in>(?:(?:(?![}][}][}]).)*\n*)+)[}][}][}]', '<div style="\g<is>">\g<in></div>', content, flags=re.IGNORECASE);

    content = re.sub('[*][[](?P<in>(?:(?![]]).)*)[]][(](?P<il>(?:(?![)]).)+)[)]', '<a class=nolink title="\g<il>">\g<in></a>', content);

    content = re.sub('^[!]\s{0,}(?P<in>(?:(?![\n]).)+)', '', content, flags=re.MULTILINE);

    content = re.sub('[*][*][*](?P<in>(?:(?![*][*][*]).)+)[*][*][*]', '<strong><i>\g<in></i></strong>', content);

    content = re.sub('^[*][*][*][*][*]', '<hr>', content, flags=re.MULTILINE);
    content = re.sub('^[*]\s[*]\s[*]', '<hr>', content, flags=re.MULTILINE);
    content = re.sub('^[-]\s[-]\s[-]', '<hr>', content, flags=re.MULTILINE);
    content = re.sub('^[-]{3,80}', '<hr>', content, flags=re.MULTILINE);

    content = re.sub('--(?P<in>(?:(?!--).)+)--', '<strike>\g<in></strike>', content);
    content = re.sub('~~(?P<in>(?:(?!~~).)+)~~', '<strike>\g<in></strike>', content);
    content = re.sub('[*][*](?P<in>(?:(?![*][*]).)+)[*][*]', '<strong>\g<in></strong>', content)
    content = re.sub('__(?P<in>(?:(?!__).)+)__', '<u>\g<in></u>', content);

    content = re.sub('{{\|(?P<in>(?:(?:(?!\|}}).)*\n*)+)\|}}', '<div class=wiki-textbox>\g<in></div>', content);

    content = re.sub('[`][`][`](?P<in>(?:(?:(?![`][`][`]).)*\n*)+)[`][`][`]', '<pre class=source-code>\g<in></pre>', content);
    content = re.sub('\s{4,4}(?P<in>(?:(?!\n).)+)', '<code class=source-code>\g<in></code><br>', content);

    content = re.sub('[[]br[]]', '<br>', content, flags=re.IGNORECASE);

    content = re.sub('[`](?P<in>(?:(?![`]).)+)[`]', '<code>\g<in></code>', content);

    content = re.sub('^\s{0,}[-]\s(?P<in>(?:(?![\n]).)+)', '<li>\g<in></li>', content, flags=re.MULTILINE);
    content = re.sub('^\s{0,}[*]\s(?P<in>(?:(?![\n]).)+)', '<li>\g<in></li>', content, flags=re.MULTILINE);
    content = re.sub('&gt;\s(?P<in>(?:(?![\n]).)+)', '<blockquote class=wiki-quote>\g<in></blockquote>', content);

    content = re.sub('[!][[](?P<in>(?:(?![]]).)+)[]][(](?P<il>(?:(?![)]).)+)[)]', '<img alt="\g<in>" src="\g<il>">', content);

    content = re.sub('[@][[](?P<in>(?:(?![]]).)*)[]][(](?P<il>(?:(?![)]).)+)[)]', '<iframe src="\g<il>">\g<in></iframe>', content);

    content = re.sub('[[](?P<in>(?:(?![]]).)+)[]][(](?P<il>(?:(?![)]).)+)[)]', '<a target=_blank href="\g<il>">\g<in></a>', content);

    content = re.sub('^[#]\s(?P<in>(?:(?![\n]).)+)', '<h1 class=wiki-heading>\g<in></h1>', content, flags=re.MULTILINE);
    content = re.sub('^[#][#]\s(?P<in>(?:(?![\n]).)+)', '<h2 class=wiki-heading>\g<in></h2>', content, flags=re.MULTILINE);
    content = re.sub('^[#][#][#]\s(?P<in>(?:(?![\n]).)+)', '<h3 class=wiki-heading>\g<in></h3>', content, flags=re.MULTILINE);
    content = re.sub('^[#][#][#][#]\s(?P<in>(?:(?![\n]).)+)', '<h4 class=wiki-heading>\g<in></h4>', content, flags=re.MULTILINE);
    content = re.sub('^[#][#][#][#][#]\s(?P<in>(?:(?![\n]).)+)', '<h5 class=wiki-heading>\g<in></h5>', content, flags=re.MULTILINE);
    content = re.sub('^[#][#][#][#][#][#]\s(?P<in>(?:(?![\n]).)+)', '<h6 class=wiki-heading>\g<in></h6>', content, flags=re.MULTILINE);

    content = re.sub('[[]date[(](?P<in>(?:(?![)]).)+)[)][]]', generateTime(getTime(), '\g<in>'), content, flags=re.IGNORECASE);
    content = re.sub('[[]datetime[(](?P<in>(?:(?![)]).)+)[)][]]', generateTime(getTime(), '\g<in>'), content, flags=re.IGNORECASE);
    content = re.sub('[[]time[(](?P<in>(?:(?![)]).)+)[)][]]', generateTime(getTime(), '\g<in>'), content, flags=re.IGNORECASE);

    content = re.sub('[[]date[]]', generateTime(getTime(), 'Y-m-d'), content, flags=re.IGNORECASE);
    content = re.sub('[[]datetime[]]', generateTime(getTime(), 'Y-m-d H:i:s'), content, flags=re.IGNORECASE);
    content = re.sub('[[]time[]]', generateTime(getTime(), 'H:i:s'), content, flags=re.IGNORECASE);

    content = re.sub('[{][{][{][#][!]folding\s(?P<it>(?:(?![\n]).)+)\n(?P<ic>(?:(?:(?![}][}][}]).)*\n*)+)[}][}][}]', '<dl class=wiki-folding><dt>\g<it></dt><dd>\g<ic></dd></dl>', content, flags=re.MULTILINE);

    try:
        content = re.sub('[{][{][{][+](?P<is>(?:(?![\s]).)+)\s(?P<in>(?:(?![}][}][}]).)+)[}][}][}]', '<span style="font-size: calc(\g<is>pt + 13pt);">\g<in></span>', content);
        content = re.sub('[{][{][{][-](?P<is>(?:(?![\s]).)+)\s(?P<in>(?:(?![}][}][}]).)+)[}][}][}]', '<span style="font-size: calc(11pt - \g<is>pt);">\g<in></span>', content);
    except:
        pass

    content = re.sub('[[][*](?P<it>(?:(?!\s).)+)\s(?P<in>(?:(?![]]).)+)[]]', '<sup><a class=wiki-footnote title="\g<in>">[\g<it>]</a></sup>', content);
    content = re.sub('[[][*]\s(?P<in>(?:(?![]]).)+)[]]', '<sup><a class=wiki-footnote title="\g<in>">[*]</a></sup>', content);

    content = re.sub('[[]youtube[(](?P<in>(?:(?![)]).)+)[)][]]', '<iframe src="https://youtube.com/embed/\g<in>"></iframe>', content, flags=re.IGNORECASE);

    content = re.sub('[{][{][{][#](?P<ic>(?:(?![\s]).)+)\s(?P<in>(?:(?![}][}][}]).)+)[}][}][}]', '<span style="color: #\g<ic>;">\g<in></span>', content);

    content = re.sub('[*](?P<in>(?:(?![*]).)+)[*]', '<i>\g<in></i>', content);

    content = re.sub('\n', '<BR />', content);

    return content;
