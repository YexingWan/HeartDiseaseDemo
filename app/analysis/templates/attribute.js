function attribute9(){
    var myChart = echarts.init(document.getElementById('main'));
        var redata={"x": ["25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79"], "male": [["-", 1, 1, 2, 1, 3, 5, 4, 2, "-", "-"], [1, "-", 1, 7, 5, 5, 9, 2, 1, 1, "-"]], "female": [["-", "-", "-", "-", "-", "-", 1, 1, 2, "-", "-"], ["-", 1, "-", 3, 4, 2, 5, 1, "-", 2, "-"]]}
        var option = {
            tooltip : {
            trigger: 'axis',
            axisPointer : {            
                type : 'shadow'        
            }
            },
            legend: {
                data: ['exercise induced angina:False', 'exercise induced angina:True'],
                y: '90%'
            },

            title: [{
                text: 'Male',
                x: '25%',
                textAlign: 'center'
            }, {
                text: 'Female',
                x: '75%',
                textAlign: 'center'
            }],


            grid: [
                {x: '7%', y: '7%', width: '38%', height: '75%'},
                {x2: '7%', y: '7%', width: '38%', height: '75%'}
            ],
            xAxis:  [{
                gridIndex:0,
                name: 'Ages',
                nameLocation: 'end',
                nameTextStyle:{fontWeight:1000},
                type: 'category',
                data: redata['x'],
                axisLabel:{rotate:45}
            },{
                gridIndex:1,
                name: 'Ages',
                nameLocation: 'end',
                nameTextStyle:{fontWeight:1000},
                type: 'category',
                data: redata['x'],
                axisLabel:{rotate:45}
            }],
            yAxis: [{
                type: 'value',
                gridIndex:0,
                name: 'Amount',
                nameLocation: 'end',
                nameTextStyle:{fontWeight:1000}
                
            },
            {gridIndex:1,type: 'value',
            name: 'Amount',
                nameLocation: 'end',
                nameTextStyle:{fontWeight:1000}}],
            series: [
                {
                    name: 'exercise induced angina:False',
                    type: 'bar',
                    stack: 'total',
                    xAxisIndex: 0,
                    yAxisIndex: 0,
                    label: {
                        normal: {
                            show: true,
                            position: 'insideRight'
                        }
                    },
                    data: redata['male'][0]

                },
                {
                    name: 'exercise induced angina:True',
                    type: 'bar',
                    stack: 'total',
                    xAxisIndex: 0,
                    yAxisIndex: 0,
                    label: {
                        normal: {
                            show: true,
                            position: 'insideRight'
                        }
                    },
                    data: redata['male'][1]

                },
                {
                    name: 'exercise induced angina:False',
                    type: 'bar',
                    stack: 'total1',
                    xAxisIndex: 1,
                    yAxisIndex: 1,
                    label: {
                        normal: {
                            show: true,
                            position: 'insideRight'
                        }
                    },
                    data: redata['female'][0]

                },
                {
                    name: 'exercise induced angina:True',
                    type: 'bar',
                    stack: 'total1',
                    xAxisIndex: 1,
                    yAxisIndex: 1,
                    label: {
                        normal: {
                            show: true,
                            position: 'insideRight'
                        }
                    },
                    data: redata['female'][1]

                }
            ]
        };
        myChart.setOption(option);
}

function attribute10(){
    var myChart = echarts.init(document.getElementById('main'));
                // 指定图表的配置项和数据
    var data = [[[63, 145, 1], [67, 160, 1], [67, 120, 2], [37, 130, 1], [56, 120, 3], [63, 130, 2], [53, 140, 1], [57, 140, 1], [56, 130, 3], [44, 120, 4], [52, 172, 1], [57, 150, 3], [48, 110, 1], [54, 140, 1], [49, 130, 1], [64, 110, 1], [58, 120, 1], [58, 132, 1], [60, 130, 2], [43, 150, 1], [40, 110, 1], [60, 117, 1], [64, 140, 1], [59, 135, 1], [44, 130, 2], [42, 140, 1], [43, 120, 1], [55, 132, 1], [61, 150, 1], [40, 140, 1], [59, 150, 1], [58, 112, 1], [51, 110, 1], [50, 150, 1], [53, 130, 2], [65, 120, 1], [44, 112, 1], [54, 124, 1], [50, 140, 1], [41, 110, 2], [54, 125, 1], [51, 125, 2], [58, 128, 2], [54, 120, 2], [60, 145, 1], [60, 140, 2], [54, 150, 1], [59, 170, 2], [46, 150, 1], [67, 125, 1], [62, 120, 2], [65, 110, 1], [44, 110, 1], [60, 125, 1], [45, 104, 1], [39, 140, 1], [68, 180, 1], [52, 120, 1], [44, 140, 1], [47, 138, 1], [66, 120, 1], [62, 130, 1], [52, 128, 3], [59, 110, 1], [52, 134, 1], [48, 122, 1], [45, 115, 1], [34, 118, 1], [49, 120, 1], [54, 108, 1], [59, 140, 2], [61, 120, 1], [39, 118, 1], [56, 125, 1], [52, 118, 1], [41, 135, 1], [58, 140, 1], [65, 135, 1], [51, 100, 1], [55, 140, 1], [65, 138, 1], [54, 110, 2], [51, 94, 1], [29, 130, 1], [70, 145, 1], [35, 120, 1], [64, 125, 1], [58, 105, 1], [47, 108, 1], [57, 165, 1], [41, 112, 1], [45, 128, 1], [52, 152, 1], [55, 160, 1], [64, 120, 1], [70, 130, 1], [58, 125, 2], [68, 118, 1], [46, 101, 1], [77, 125, 1], [48, 124, 2], [57, 132, 1], [52, 138, 1], [35, 126, 1], [70, 160, 1], [53, 142, 1], [64, 145, 1], [57, 152, 1], [52, 108, 1], [56, 132, 1], [43, 130, 1], [42, 148, 1], [59, 178, 1], [42, 120, 2], [66, 160, 2], [54, 192, 1], [50, 129, 1], [67, 100, 1], [69, 160, 1], [59, 160, 1], [43, 110, 1], [45, 142, 1], [50, 144, 1], [55, 130, 1], [38, 120, 1], [52, 112, 1], [59, 138, 1], [53, 123, 1], [47, 112, 1], [66, 112, 1], [49, 118, 1], [54, 122, 1], [46, 120, 1], [61, 134, 1], [47, 110, 1], [52, 125, 1], [62, 128, 1], [57, 110, 2], [58, 146, 1], [64, 128, 1], [43, 115, 1], [70, 156, 1], [57, 124, 1], [61, 138, 1], [42, 136, 1], [59, 126, 1], [40, 152, 1], [42, 130, 1], [61, 140, 1], [46, 140, 1], [59, 134, 1], [64, 170, 1], [57, 154, 1], [47, 130, 1], [35, 122, 1], [61, 148, 1], [58, 114, 1], [41, 120, 1], [59, 164, 1], [45, 110, 1], [68, 144, 1], [57, 130, 1], [38, 138, 1]], [[41, 130, 1], [62, 140, 2], [57, 120, 1], [56, 140, 1], [48, 130, 1], [58, 150, 1], [50, 120, 2], [66, 150, 1], [69, 140, 1], [65, 150, 1], [71, 160, 1], [61, 130, 1], [65, 140, 1], [41, 105, 1], [51, 130, 2], [46, 142, 1], [54, 135, 1], [65, 155, 1], [65, 160, 1], [51, 140, 1], [53, 128, 1], [53, 138, 1], [62, 160, 1], [44, 108, 1], [63, 135, 1], [60, 150, 2], [57, 128, 1], [71, 110, 1], [61, 145, 1], [43, 132, 1], [35, 138, 1], [63, 150, 1], [45, 130, 1], [56, 200, 1], [62, 124, 1], [43, 122, 1], [55, 135, 1], [60, 102, 1], [42, 102, 1], [67, 115, 1], [58, 100, 1], [54, 132, 1], [45, 112, 1], [59, 174, 1], [56, 134, 1], [60, 158, 1], [63, 140, 1], [62, 138, 1], [68, 120, 1], [45, 138, 1], [50, 110, 1], [64, 180, 1], [62, 150, 1], [37, 120, 1], [66, 178, 1], [46, 105, 1], [46, 138, 1], [64, 130, 1], [39, 94, 1], [63, 108, 1], [67, 152, 1], [52, 136, 1], [55, 180, 1], [74, 120, 1], [54, 160, 1], [49, 134, 1], [41, 126, 1], [60, 120, 1], [51, 120, 1], [67, 106, 1], [76, 140, 1], [44, 118, 1], [58, 136, 1], [71, 112, 1], [66, 146, 1], [39, 138, 1], [58, 130, 1], [55, 128, 1], [58, 170, 1], [63, 124, 1]]];
    var schema = [
        {name: 'AGE', index: 0, text: 'Age'},
        {name: 'oldpeak', index: 1, text: 'Blood Pressure'},
        {name: 'Amount', index: 2, text: 'Amount'}
    ];
    var option = {
        backgroundColor: new echarts.graphic.RadialGradient(0.3, 0.3, 0.8, [{
        offset: 0,
        color: '#f7f8fa'}, 
        {
            offset: 1,
            color: '#cdd0d5'
        }]),
        legend: {
            right: 10,
            data: ['Male', 'Female']
        },
        tooltip: {
            padding: 10,
            backgroundColor: '#222',
            borderColor: '#777',
            borderWidth: 1,
            formatter: function (obj) {
                var value = obj.value;
                return  schema[0].text + ': ' + value[0] + '<br>'
                    + schema[1].text + '：' + value[1] + '<br>'
                    + schema[2].text + '：' + value[2] + '<br>';
            }
        },
        xAxis: {
            min:25,
            name: 'Ages',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000},
            splitLine: {
                lineStyle: {
                    type: 'dashed'
                }
            }
        },
        yAxis: {
            name: 'oldpeak',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000},
            splitLine: {
                lineStyle: {
                    type: 'dashed'
                }
            },
            scale: true
        },
        series: [{
            name: 'Male',
            data: data[0],
            type: 'scatter',
            symbolSize: function (data) {
                return Math.sqrt(data[2]) / 0.15;
            },
            itemStyle: {
                normal: {
                    shadowBlur: 10,
                    shadowColor: 'rgba(120, 36, 50, 0.5)',
                    shadowOffsetY: 5,
                    color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                        offset: 0,
                        color: 'rgb(251, 118, 123)'
                    }, {
                        offset: 1,
                        color: 'rgb(204, 46, 72)'
                    }])
                }
            }
        }, {
            name: 'Female',
            data: data[1],
            type: 'scatter',
            symbolSize: function (data) {
                return Math.sqrt(data[2]) / 0.15;
            },
            itemStyle: {
                normal: {
                    shadowBlur: 10,
                    shadowColor: 'rgba(25, 100, 150, 0.5)',
                    shadowOffsetY: 5,
                    color: new echarts.graphic.RadialGradient(0.4, 0.3, 1, [{
                        offset: 0,
                        color: 'rgb(129, 227, 238)'
                    }, {
                        offset: 1,
                        color: 'rgb(25, 183, 207)'
                    }])
                }
            }
        }]
    };
    myChart.setOption(option);
}


function attribute11(){
    var myChart = echarts.init(document.getElementById('main'));
                // 指定图表的配置项和数据
    var redata={"x": ["25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79"], "male": [["-", 1, 1, 2, 1, 3, 5, 4, 2, "-", "-"], [1, "-", 1, 7, 5, 5, 9, 2, 1, 1, "-"],["-", 1, 1, 2, 1, 3, 5, 4, 2, "-", "-"]], "female": [["-", "-", "-", "-", "-", "-", 1, 1, 2, "-", "-"], ["-", 1, "-", 3, 4, 2, 5, 1, "-", 2, "-"],["-", "-", "-", "-", "-", "-", 1, 1, 2, "-", "-"]]}
    var option = {
        tooltip : {
        trigger: 'axis',
        axisPointer : {            
            type : 'shadow'        
        }
        },
        legend: {
            data: ['the slope of the peak exercise ST segment:1', 'the slope of the peak exercise ST segment:2','the slope of the peak exercise ST segment:3'],
            y: '90%'
        },

        title: [{
            text: 'Male',
            x: '25%',
            textAlign: 'center'
        }, {
            text: 'Female',
            x: '75%',
            textAlign: 'center'
        }],


        grid: [
            {x: '7%', y: '7%', width: '38%', height: '75%'},
            {x2: '7%', y: '7%', width: '38%', height: '75%'}
        ],
        xAxis:  [{
            gridIndex:0,
            name: 'Ages',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000},
            type: 'category',
            data: redata['x'],
            axisLabel:{rotate:45}
        },{
            gridIndex:1,
            name: 'Ages',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000},
            type: 'category',
            data: redata['x'],
            axisLabel:{rotate:45}
        }],
        yAxis: [{
            type: 'value',
            gridIndex:0,
            name: 'Amount',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000}
            
        },
        {gridIndex:1,type: 'value',
        name: 'Amount',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000}}],
        series: [
            {
                name: 'the slope of the peak exercise ST segment:1',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][0]

            },
            {
                name: 'the slope of the peak exercise ST segment:2',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][1]

            },
            {
                name: 'the slope of the peak exercise ST segment:3',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][2]

            },
            {
                name: 'the slope of the peak exercise ST segment:1',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][0]

            },
            {
                name: 'the slope of the peak exercise ST segment:2',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][1]

            },
            {
                name: 'the slope of the peak exercise ST segment:3',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][2]

            }
            
        ]
    };
    myChart.setOption(option);
}

function attribute12(){
    var myChart = echarts.init(document.getElementById('main'));
                // 指定图表的配置项和数据
    var redata={"x": ["25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79"], "male": [["-", 1, 1, 2, 1, 3, 5, 4, 2, "-", "-"], [1, "-", 1, 7, 5, 5, 9, 2, 1, 1, "-"],["-", 1, 1, 2, 1, 3, 5, 4, 2, "-", "-"],["-", 1, 1, 2, 1, 3, 5, 4, 2, "-", "-"]], "female": [["-", "-", "-", "-", "-", "-", 1, 1, 2, "-", "-"], ["-", 1, "-", 3, 4, 2, 5, 1, "-", 2, "-"],["-", "-", "-", "-", "-", "-", 1, 1, 2, "-", "-"],["-", "-", "-", "-", "-", "-", 1, 1, 2, "-", "-"]]}
    var option = {
        tooltip : {
        trigger: 'axis',
        axisPointer : {            
            type : 'shadow'        
        }
        },
        legend: {
            data: ['vessels colored:0', 'vessels colored:1','vessels colored:2','vessels colored:3'],
            y:'90%'
        },

        title: [{
            text: 'Male',
            x: '25%',
            textAlign: 'center'
        }, {
            text: 'Female',
            x: '75%',
            textAlign: 'center'
        }],


        grid: [
            {x: '7%', y: '7%', width: '38%', height: '75%'},
            {x2: '7%', y: '7%', width: '38%', height: '75%'}
        ],
        xAxis:  [{
            gridIndex:0,
            name: 'Ages',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000},
            type: 'category',
            data: redata['x'],
            axisLabel:{rotate:45}
        },{
            gridIndex:1,
            name: 'Ages',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000},
            type: 'category',
            data: redata['x'],
            axisLabel:{rotate:45}
        }],
        yAxis: [{
            type: 'value',
            gridIndex:0,
            name: 'Amount',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000}
            
        },
        {gridIndex:1,type: 'value',
        name: 'Amount',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000}}],
        series: [
            {
                name: 'vessels colored:0',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][0]

            },
            {
                name: 'vessels colored:1',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][1]

            },
            {
                name: 'vessels colored:2',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][2]

            },
            {
                name: 'vessels colored:3',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][3]
            },
            {
                name: 'vessels colored:0',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][0]

            },
            {
                name: 'vessels colored:1',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][1]

            },
            {
                name: 'vessels colored:2',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][2]

            },
            {
                name: 'vessels colored:3',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][3]

            }
        ]
    };
        myChart.setOption(option);
}


function attribute13(){
    var myChart = echarts.init(document.getElementById('main'));
                // 指定图表的配置项和数据
    var redata={"x": ["25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79"], "male": [["-", 1, 1, 2, 1, 3, 5, 4, 2, "-", "-"], [1, "-", 1, 7, 5, 5, 9, 2, 1, 1, "-"],["-", 1, 1, 2, 1, 3, 5, 4, 2, "-", "-"]], "female": [["-", "-", "-", "-", "-", "-", 1, 1, 2, "-", "-"], ["-", 1, "-", 3, 4, 2, 5, 1, "-", 2, "-"],["-", "-", "-", "-", "-", "-", 1, 1, 2, "-", "-"]]}
    var option = {
        tooltip : {
        trigger: 'axis',
        axisPointer : {            
            type : 'shadow'        
        }
        },
        legend: {
            data: ['thal: normal', 'thal: fixed defect','thal: reversable defect'],
            y: '90%'
        },

        title: [{
            text: 'Male',
            x: '25%',
            textAlign: 'center'
        }, {
            text: 'Female',
            x: '75%',
            textAlign: 'center'
        }],


        grid: [
            {x: '7%', y: '7%', width: '38%', height: '75%'},
            {x2: '7%', y: '7%', width: '38%', height: '75%'}
        ],
        xAxis:  [{
            gridIndex:0,
            name: 'Ages',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000},
            type: 'category',
            data: redata['x'],
            axisLabel:{rotate:45}
        },{
            gridIndex:1,
            name: 'Ages',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000},
            type: 'category',
            data: redata['x'],
            axisLabel:{rotate:45}
        }],
        yAxis: [{
            type: 'value',
            gridIndex:0,
            name: 'Amount',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000}
            
        },
        {gridIndex:1,type: 'value',
        name: 'Amount',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000}}],
        series: [
            {
                name: 'thal: normal',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][0]

            },
            {
                name: 'thal: fixed defect',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][1]

            },
            {
                name: 'thal: reversable defect',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][2]

            },
            {
                name: 'thal: normal',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][0]

            },
            {
                name: 'thal: fixed defect',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][1]

            },
            {
                name: 'thal: reversable defect',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][2]

            }
            
        ]
    };
    myChart.setOption(option);
}

function attribute14(){
    var myChart = echarts.init(document.getElementById('main'));
                // 指定图表的配置项和数据
    var redata={"x": ["25-29", "30-34", "35-39", "40-44", "45-49", "50-54", "55-59", "60-64", "65-69", "70-74", "75-79"], "male": [["-", 1, 1, 2, 1, 3, 5, 4, 2, "-", "-"], [1, "-", 1, 7, 5, 5, 9, 2, 1, 1, "-"],["-", 1, 1, 2, 1, 3, 5, 4, 2, "-", "-"],["-", 1, 1, 2, 1, 3, 5, 4, 2, "-", "-"], [1, "-", 1, 7, 5, 5, 9, 2, 1, 1, "-"]], "female": [["-", "-", "-", "-", "-", "-", 1, 1, 2, "-", "-"], ["-", 1, "-", 3, 4, 2, 5, 1, "-", 2, "-"],["-", "-", "-", "-", "-", "-", 1, 1, 2, "-", "-"],["-", 1, 1, 2, 1, 3, 5, 4, 2, "-", "-"], [1, "-", 1, 7, 5, 5, 9, 2, 1, 1, "-"]]}
    var option = {
        tooltip : {
        trigger: 'axis',
        axisPointer : {            
            type : 'shadow'        
        }
        },
        legend: {
            data: ['target: 0', 'target: 1','target: 2','target: 3','target: 4'],
            y: '90%'
        },

        title: [{
            text: 'Male',
            x: '25%',
            textAlign: 'center'
        }, {
            text: 'Female',
            x: '75%',
            textAlign: 'center'
        }],


        grid: [
            {x: '7%', y: '7%', width: '38%', height: '75%'},
            {x2: '7%', y: '7%', width: '38%', height: '75%'}
        ],
        xAxis:  [{
            gridIndex:0,
            name: 'Ages',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000},
            type: 'category',
            data: redata['x'],
            axisLabel:{rotate:45}
        },{
            gridIndex:1,
            name: 'Ages',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000},
            type: 'category',
            data: redata['x'],
            axisLabel:{rotate:45}
        }],
        yAxis: [{
            type: 'value',
            gridIndex:0,
            name: 'Amount',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000}
            
        },
        {gridIndex:1,type: 'value',
        name: 'Amount',
            nameLocation: 'end',
            nameTextStyle:{fontWeight:1000}}],
        series: [
            {
                name: 'target: 0',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][0]

            },
            {
                name: 'target: 1',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][1]

            },
            {
                name: 'target: 2',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][2]

            },
            {
                name: 'target: 3',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][3]

            },
            {
                name: 'target: 4',
                type: 'bar',
                stack: 'total',
                xAxisIndex: 0,
                yAxisIndex: 0,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['male'][4]

            },
            {
                name: 'target: 0',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][0]

            },
            {
                name: 'target: 1',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][1]

            },
            {
                name: 'target: 2',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][2]

            },
            {
                name: 'target: 3',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][3]

            },
            {
                name: 'target: 4',
                type: 'bar',
                stack: 'total1',
                xAxisIndex: 1,
                yAxisIndex: 1,
                label: {
                    normal: {
                        show: true,
                        position: 'insideRight'
                    }
                },
                data: redata['female'][4]

            }
            
        ]
    };
    myChart.setOption(option);
}