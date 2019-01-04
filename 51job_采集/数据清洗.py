# coding:utf8
import xlrd
import codecs
import re


# 加载Excel数据，获得工作表和行数
def load_from_xlsx(file):
    data = xlrd.open_workbook(file)
    table0 = data.sheet_by_name('Sheet1')
    nrows = table0.nrows
    return table0, nrows


# 利用正则表达式提取月薪，把待遇规范成千/月的形式
def get_salary(salary):
    if '-' in salary:  # 针对1-2万/月或者10-20万/年的情况，包含-
        low_salary = re.findall(re.compile('(\d*\.?\d+)'), salary)[0]
        high_salary = re.findall(re.compile('(\d?\.?\d+)'), salary)[1]
        if u'万' in salary and u'年' in salary:  # 单位统一成千/月的形式
            low_salary = float(low_salary) / 12 * 10
            high_salary = float(high_salary) / 12 * 10
        elif u'万' in salary and u'月' in salary:
            low_salary = float(low_salary) * 10
            high_salary = float(high_salary) * 10
    else:  # 针对20万以上/年和100元/天这种情况，不包含-，取最低工资，没有最高工资
        low_salary = re.findall(re.compile('(\d*\.?\d+)'), salary)[0]
        high_salary = ""
        if u'万' in salary and u'年' in salary:  # 单位统一成千/月的形式
            low_salary = float(low_salary) / 12 * 10
        elif u'万' in salary and u'月' in salary:
            low_salary = float(low_salary) * 10
        elif u'元' in salary and u'天' in salary:
            low_salary = float(low_salary) / 1000 * 21  # 每月工作日21天
    return low_salary, high_salary


def main():
    data = load_from_xlsx(r'new51job.xlsx')
    table, nrows = data[0], data[1]
    print('一共有{}行数据，开始清洗数据'.format(nrows))
    for i in range(1, nrows):
        id = table.row_values(i)[0]
        company = table.row_values(i)[1]
        position = table.row_values(i)[2]
        education = table.row_values(i)[3]
        welfare = table.row_values(i)[4]
        salary = table.row_values(i)[5]
        area = table.row_values(i)[6][:2]  # 地区取到城市，把区域去掉
        companytype = table.row_values(i)[7]
        companysize = table.row_values(i)[8]
        field = table.row_values(i)[9]
        experience = table.row_values(i)[10]
        responsibility = table.row_values(i)[11]
        requirement = table.row_values(i)[12]
        if salary:  # 如果待遇这栏不为空，计算最低最高待遇
            getsalary = get_salary(salary)
            low_salary = getsalary[0]
            high_salary = getsalary[1]
        else:
            low_salary = high_salary = ""
        print('正在写入第{}条，最低工资是{}k,最高工资是{}k'.format(i, low_salary, high_salary))
        output = '{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n'.format(id, company, position, education,
                                                                                   welfare, low_salary, high_salary,
                                                                                   area, companytype, companysize,
                                                                                   field, experience, responsibility,
                                                                                   requirement)
        f = codecs.open('51jobanaly.xls', 'a+')
        f.write(output)
        f.close()


if __name__ == '__main__':
    main()
