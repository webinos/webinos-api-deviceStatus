{
  'variables': {
    'module_name': 'devicestatus',#Specify the module name here
	#you may override the variables found in node_module.gypi here or through command line
  },
  'targets': [
    {
	  # Needed declarations for the target
	  'target_name': '<(module_name)',
	  'product_name':'nativedevicestatus',
	  'sources': [ #Specify your source files here
			'src/nativedevicestatus.cc',
			'src/aspects.cc',
			'src/utils.cc',
		],
		'conditions': [
			['OS=="freebsd" or OS=="openbsd" or OS=="solaris" or (OS=="linux")', {
				'defines': ['OS_LINUX'],
				'sources': [
					'src/aspects/platform/linux/battery.cc',
					'src/aspects/platform/linux/cpu.cc',
					'src/aspects/platform/linux/device.cc',
					'src/aspects/platform/linux/display.cc',
					'src/aspects/platform/linux/input_device.cc',
					'src/aspects/platform/linux/memory_unit.cc',
					'src/aspects/platform/linux/operating_system.cc',
					'src/aspects/platform/linux/wifi_hardware.cc',
					'src/aspects/platform/linux/wifi_network.cc',
					'src/aspects/platform/linux/wired_network.cc'
				]
			}],
			[ 'OS=="win"', {
				'defines': ['OS_WIN'],
				'sources': [
					'src/aspects/platform/win/battery.cc',
					'src/aspects/platform/win/cpu.cc',
					'src/aspects/platform/win/device.cc',
					'src/aspects/platform/win/display.cc',
					'src/aspects/platform/win/input_device.cc',
					'src/aspects/platform/win/memory_unit.cc',
					'src/aspects/platform/win/operating_system.cc',
					'src/aspects/platform/win/wifi_hardware.cc',
					'src/aspects/platform/win/wired_network.cc'
				]
			 }],
			[ 'OS=="mac"', {
				'defines': ['OS_LINUX'],
				'sources': [
					'src/aspects/platform/mac/battery.cc',
					'src/aspects/platform/mac/camera.cc',
					'src/aspects/platform/mac/cellular_hardware.cc',
					'src/aspects/platform/mac/cellular_network.cc',
					'src/aspects/platform/mac/cpu.cc',
					'src/aspects/platform/mac/device.cc',
					'src/aspects/platform/mac/display.cc',
					'src/aspects/platform/mac/input_control.cc',
					'src/aspects/platform/mac/input_device.cc',
					'src/aspects/platform/mac/memory_unit.cc',
					'src/aspects/platform/mac/operating_system.cc',
					'src/aspects/platform/mac/parental_rating.cc',
					'src/aspects/platform/mac/web_runtime.cc',
					'src/aspects/platform/mac/wifi_hardware.cc',
					'src/aspects/platform/mac/wifi_network.cc',
					'src/aspects/platform/mac/wired_network.cc'
				]
			 }],

		],
    },
  ] # end targets
}

