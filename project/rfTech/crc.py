#!/usr/bin/env python
#-*- coding: utf-8 -*-

# crc.py
# Based on http://zorc.breitbandkatze.de/crctester.c
# author: Diego Manenti Martins - dmmartins@gmail.com

class CRC:
    def __init__(self, order=16, poly= 0x8005, initial=0, final_xor=0, reverse=True):
    # def __init__(self, order, poly, initial=0, final_xor=0, reverse=True):
    # def __init__(self, order, poly, initial=0, final_xor=0, reverse=False):
        # print('order:{}'.format(order))
        if order < 1 or order >32:
            print('OrderError:', Order)
            # raise ValueError, 'Polynom order must be between 1 to 32.'

        self.order = order
        self.mask = (1 << order) - 1

        # Polynomial used on calculation
        if poly != (poly & self.mask):
            print('Invalid polynom.')
            # raise ValueError, 'Invalid polynom.'

        self.poly = poly

        # Initial value for crc calculation
        if initial != (initial & self.mask):
            print('Invalid initial value.')
            # raise ValueError, 'Invalid initial value.'

        self.crc = initial

        # Final XOR applied to result
        if final_xor != (final_xor & self.mask):
            print('Invalid final XOR value.')
            # raise ValueError, 'Invalid final XOR value.'

        self.final_xor = final_xor

        # Reverse input data
        self.reverse = reverse

    def update(self, data):
        # Reflect data if necessary
        if self.reverse:
            get_data = self._reflect
        else:
            get_data = lambda x, bits=None: x

        self.crc = get_data(self.crc, self.order)
        crc_high_bit = 1 << (self.order - 1)

        for char in data:
            # byte = get_data(ord(char))
            byte = get_data(char)
            # Mask bits from 0x80 to 0x01
            for x in range(7, -1, -1):
                bit = 1 << x

                # If bit is 1 OR EXLUSIVE crc shift left carry out, apply polynomial
                if bool(byte & bit) ^ bool(self.crc & crc_high_bit):
                    self.crc = self.crc << 1
                    self.crc = self.crc ^ self.poly
                else:
                    self.crc = self.crc << 1

        # Reflect and apply final XOR
        self.crc = (get_data(self.crc, self.order) & self.mask) ^ self.final_xor
        return self.crc

    def _reflect(self, data, bits=8):
        ''' Reflect bits. Eg 00101010 > 01010100. '''
        x = 1 << (bits - 1)
        y = 1
        r = 0
        while x:
                if data & x:
                    r |= y
                x = x >> 1
                y = y << 1
        return r


# # Predefined CRC calcs
# class CRC16(CRC):
#     '''
#     CRC-16
#     Order = 16
#     Polynomial = 0x8005
#     Initial value = 0xffff
#     Final XOR = 0
#     Reverse = True
#     '''
#     def __init__(self):
#         CRC.__init__(self, 16, 0x8005, 0xffff, 0, True)
#
#
# class CRC32(CRC):
#     '''
#     CRC-32
#     Order = 32
#     Polynomial = 0x4c11db7
#     Initial value = 0xffffffff
#     Final XOR = 0xffffffff
#     Reverse = True
#     '''
#     def __init__(self):
#         CRC.__init__(self, 32, 0x4c11db7, 0xffffffff, 0xffffffff, True)

# if __name__ == '__main__':
#     from doctest import testmod
#     print('This is Crc Module')
    # testmod()
