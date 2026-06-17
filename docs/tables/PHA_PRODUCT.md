# PHA_PRODUCT

> Table is created by batch update process and formulary listing process to allow selection by dynamic criteria. Also used to generate formulary export spreadsheet.

**Description:** Pharmacy Product  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 222

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AHFS_CODE` | VARCHAR(6) |  |  | Therapeutic Class string |
| 2 | `ALTERNATE_DISPENSE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Alternate Dispense Category for this product |
| 3 | `ALT_SEL_CATEGORY_ID` | DOUBLE | NOT NULL |  | alt_sel_category id associated with ahfs_code |
| 4 | `AWP` | DOUBLE |  |  | Average Wholesale price |
| 5 | `AWP_FACTOR` | DOUBLE |  |  | Same as dispense factor, this is greater than 0 if there's a different unit of measure specified for dispense quantity than specified for base unit of measure. |
| 6 | `BASE_ISSUE_FACTOR` | DOUBLE |  |  | Ratio identifying smallest unit of issue for pharmacy product |
| 7 | `BASE_PACKAGE_SIZE` | DOUBLE |  |  | Size of smallest dispensible unit |
| 8 | `BASE_PACKAGE_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measure code_value for smallest dispensible unit |
| 9 | `BRAND_NAME` | VARCHAR(100) |  |  | Manufacturer brand/trade name for the product |
| 10 | `BRAND_NAME2` | VARCHAR(100) |  |  | Second manufacturer brand/trade name for the product |
| 11 | `BRAND_NAME2_PRIMARY` | DOUBLE |  |  | Identifies if Brand Name 2 is primary. 0 = not primary, 1 = primary. |
| 12 | `BRAND_NAME3` | VARCHAR(100) |  |  | Third manufacturer brand/trade name for the product |
| 13 | `BRAND_NAME3_PRIMARY` | DOUBLE |  |  | Identifies if Brand Name 3 is primary. 0 = not primary, 1 = primary. |
| 14 | `BRAND_NAME_KEY` | VARCHAR(100) |  |  | Uppercase manufacturer brand/trade name - used for sorting on the report |
| 15 | `BRAND_NAME_PRIMARY` | DOUBLE |  |  | Identifies if Brand Name is primary. 0 = not primary, 1 = primary. |
| 16 | `CATALOG_CD` | DOUBLE | NOT NULL |  | Order Catalog code associated with product |
| 17 | `CDM` | VARCHAR(30) |  |  | Charge Description Master Identifier String |
| 18 | `COMMENT1_ID` | DOUBLE | NOT NULL |  | ID for dispenseing Comment 1 |
| 19 | `COMMENT1_TEXT` | VARCHAR(255) |  |  | Text of Comment1 |
| 20 | `COMMENT1_TYPE` | DOUBLE |  |  | Determines whether note appears of label, MAR of Fill List |
| 21 | `COMMENT2_ID` | DOUBLE | NOT NULL |  | ID For 2nd Dispensing comment |
| 22 | `COMMENT2_TEXT` | VARCHAR(255) |  |  | Text of Comment2 |
| 23 | `COMMENT2_TYPE` | DOUBLE |  |  | Identifies whether comment should appear on label, mar or fill |
| 24 | `COMPOUND_TEXT` | VARCHAR(255) |  |  | Text of compounding instructions |
| 25 | `COMPOUND_TEXT_ID` | DOUBLE | NOT NULL |  | ID for compounding Instructions |
| 26 | `CONTINUOUS_FILTER_IND` | DOUBLE |  |  | Used to indicate product should appear on product selection lists including continuous order products |
| 27 | `COST1` | DOUBLE |  |  | Primary cost associated with product |
| 28 | `COST2` | DOUBLE |  |  | Secondary cost associated with product |
| 29 | `DC_DISPLAY_DAYS` | DOUBLE |  |  | number of days to display the product in the patients profile after the product has been discontinued. |
| 30 | `DC_INTERACTION_DAYS` | DOUBLE |  |  | Number of days drug stays active in patients body for interaction checking |
| 31 | `DEFAULT_PAR_DOSES` | DOUBLE |  |  | Number of doses to default for PRN orders |
| 32 | `DEF_DURUNIT_ID` | DOUBLE | NOT NULL |  | Order Entry Field containing the Default Duration Units |
| 33 | `DEF_DURUNIT_MEAN` | DOUBLE |  |  | Order Entry Field meaning for default duration units |
| 34 | `DEF_DURUNIT_NEW` | DOUBLE |  |  | New value for default duration units - only valued during batch update process |
| 35 | `DEF_DURUNIT_VAL` | DOUBLE |  |  | Present code_value for default duration units. |
| 36 | `DEF_DUR_ID` | DOUBLE | NOT NULL |  | Order entry field id for default duration |
| 37 | `DEF_DUR_MEAN` | DOUBLE |  |  | Order Entry Field meaning for default duration |
| 38 | `DEF_DUR_NEW` | DOUBLE |  |  | New value for default duration - only valued during batch update process |
| 39 | `DEF_DUR_VAL` | DOUBLE |  |  | Present value for default duration. |
| 40 | `DEF_FREQ_ID` | DOUBLE | NOT NULL |  | order entry field containing default frequency |
| 41 | `DEF_FREQ_MEAN` | DOUBLE |  |  | Order entry field meaning for default frequency |
| 42 | `DEF_FREQ_NEW` | DOUBLE |  |  | New value for default frequency - only valued during batch update process |
| 43 | `DEF_FREQ_VAL` | DOUBLE |  |  | Present code value for default frequency |
| 44 | `DEF_FTDOSE_ID` | DOUBLE | NOT NULL |  | Order Entry default for free text dose |
| 45 | `DEF_FTDOSE_MEAN` | DOUBLE |  |  | Order entry field meaning for free text dose |
| 46 | `DEF_FTDOSE_NEW` | VARCHAR(100) |  |  | New Value for free text dose - used in bactch update mode |
| 47 | `DEF_FTDOSE_VAL` | VARCHAR(100) |  |  | Value for free text dose |
| 48 | `DEF_PRN_ID` | DOUBLE | NOT NULL |  | Order entry default for SCH/PRN indicator |
| 49 | `DEF_PRN_MEAN` | DOUBLE |  |  | OE field meaning ID for sch/PRN incidicator |
| 50 | `DEF_PRN_VAL` | DOUBLE |  |  | Value of sch/prn indicator |
| 51 | `DEF_ROUTE_ID` | DOUBLE | NOT NULL |  | order entry field containing default route_cd |
| 52 | `DEF_ROUTE_MEAN` | DOUBLE |  |  | Order entry field meaning for default route |
| 53 | `DEF_ROUTE_NEW` | DOUBLE |  |  | New code value for default route - only valued during batch update process |
| 54 | `DEF_ROUTE_VAL` | DOUBLE |  |  | Present code_value for default route. |
| 55 | `DEF_STOP_ID` | DOUBLE | NOT NULL |  | order entry field containing default stop type code_value |
| 56 | `DEF_STOP_MEAN` | DOUBLE |  |  | Order entry field meaning for default stop type |
| 57 | `DEF_STOP_NEW` | DOUBLE |  |  | New code value for default stop type- only valued during batch update process |
| 58 | `DEF_STOP_VAL` | DOUBLE |  |  | Present code_value for default stop type |
| 59 | `DEF_STRUNIT_ID` | DOUBLE | NOT NULL |  | order entry field containing default strength units code_value |
| 60 | `DEF_STRUNIT_MEAN` | DOUBLE |  |  | Order entry field meaning for default strength units |
| 61 | `DEF_STRUNIT_NEW` | DOUBLE |  |  | New code value for default strength units - only valued during batch update process |
| 62 | `DEF_STRUNIT_VAL` | DOUBLE |  |  | Present code_value for default strength units |
| 63 | `DEF_STR_ID` | DOUBLE | NOT NULL |  | order entry field containing default strength |
| 64 | `DEF_STR_MEAN` | DOUBLE |  |  | Order entry field meaning for default strength |
| 65 | `DEF_STR_NEW` | DOUBLE |  |  | New value for default strength - only valued during batch update process |
| 66 | `DEF_STR_VAL` | DOUBLE |  |  | Present value for default strength |
| 67 | `DEF_VOLUNIT_ID` | DOUBLE | NOT NULL |  | order entry field containing default volume units |
| 68 | `DEF_VOLUNIT_MEAN` | DOUBLE |  |  | Order entry field meaning for default volume units |
| 69 | `DEF_VOLUNIT_NEW` | DOUBLE |  |  | New code value for default volume units - only valued during batch update process |
| 70 | `DEF_VOLUNIT_VAL` | DOUBLE |  |  | Present code_value for default volume units |
| 71 | `DEF_VOL_ID` | DOUBLE | NOT NULL |  | order entry field containing default volume |
| 72 | `DEF_VOL_MEAN` | DOUBLE |  |  | Order entry field meaning for default volume |
| 73 | `DEF_VOL_NEW` | DOUBLE |  |  | New value for default volume - only valued during batch update process |
| 74 | `DEF_VOL_VAL` | DOUBLE |  |  | Present value for default volume |
| 75 | `DILUENT_ID` | DOUBLE | NOT NULL |  | Item Id for default diluent - presently not used |
| 76 | `DILUENT_VOLUME` | DOUBLE |  |  | Volume for default diluent - presently not used |
| 77 | `DISPENSE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Primary dispense category cd for product |
| 78 | `DISPENSE_FROM_FLAG` | DOUBLE |  |  | Identify where a medication is dispensed from |
| 79 | `DISPENSE_QTY` | DOUBLE |  |  | Amount to be dispensed |
| 80 | `DISPENSE_QTY_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measure for dispense amount |
| 81 | `DIVISIBLE_IND` | DOUBLE |  |  | Indicates the product can be divided into smaller units |
| 82 | `FAC_ALL` | DOUBLE |  |  | Indicates whether product is for all facilities or not. 0 = not, 1 = all facilities. |
| 83 | `FAC_CERN1` | DOUBLE |  |  | multi facitliy logic |
| 84 | `FAC_CERN10` | DOUBLE |  |  | multi facitliy logic |
| 85 | `FAC_CERN11` | DOUBLE |  |  | multi facitliy logic |
| 86 | `FAC_CERN12` | DOUBLE |  |  | multi facitliy logic |
| 87 | `FAC_CERN13` | DOUBLE |  |  | multi facitliy logic |
| 88 | `FAC_CERN14` | DOUBLE |  |  | multi facitliy logic |
| 89 | `FAC_CERN15` | DOUBLE |  |  | multi facitliy logic |
| 90 | `FAC_CERN16` | DOUBLE |  |  | multi facitliy logic |
| 91 | `FAC_CERN17` | DOUBLE |  |  | multi facitliy logic |
| 92 | `FAC_CERN18` | DOUBLE |  |  | multi facitliy logic |
| 93 | `FAC_CERN19` | DOUBLE |  |  | multi facitliy logic |
| 94 | `FAC_CERN2` | DOUBLE |  |  | multi facitliy logic |
| 95 | `FAC_CERN20` | DOUBLE |  |  | multi facitliy logic |
| 96 | `FAC_CERN21` | DOUBLE |  |  | multi facitliy logic |
| 97 | `FAC_CERN22` | DOUBLE |  |  | multi facitliy logic |
| 98 | `FAC_CERN23` | DOUBLE |  |  | multi facitliy logic |
| 99 | `FAC_CERN24` | DOUBLE |  |  | multi facitliy logic |
| 100 | `FAC_CERN25` | DOUBLE |  |  | multi facitliy logic |
| 101 | `FAC_CERN26` | DOUBLE |  |  | multi facitliy logic |
| 102 | `FAC_CERN27` | DOUBLE |  |  | multi facitliy logic |
| 103 | `FAC_CERN28` | DOUBLE |  |  | multi facitliy logic |
| 104 | `FAC_CERN29` | DOUBLE |  |  | multi facitliy logic |
| 105 | `FAC_CERN3` | DOUBLE |  |  | multi facitliy logic |
| 106 | `FAC_CERN30` | DOUBLE |  |  | multi facitliy logic |
| 107 | `FAC_CERN4` | DOUBLE |  |  | multi facitliy logic |
| 108 | `FAC_CERN5` | DOUBLE |  |  | multi facitliy logic |
| 109 | `FAC_CERN6` | DOUBLE |  |  | multi facitliy logic |
| 110 | `FAC_CERN7` | DOUBLE |  |  | multi facitliy logic |
| 111 | `FAC_CERN8` | DOUBLE |  |  | multi facitliy logic |
| 112 | `FAC_CERN9` | DOUBLE |  |  | multi facitliy logic |
| 113 | `FORMULARY_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates whether a product is approved for ordering, dispensing and adminstering to a patient by the organization or benefits manager |
| 114 | `FORM_CD` | DOUBLE | NOT NULL |  | The dosage form the product is supplied in . |
| 115 | `GCR_CKI` | VARCHAR(100) |  |  | Cerner knowledge index value for generic cross reference. CKI is MUL.DRUG! |
| 116 | `GCR_CODE` | VARCHAR(6) |  |  | Generic Cross Reference code as defined by Medical economics (Redbook/Micromedex) - NO LONGER IN ACTIVE USE |
| 117 | `GCR_DESC` | VARCHAR(255) |  |  | Generic Cross reference description |
| 118 | `GENERIC_NAME` | VARCHAR(100) |  |  | Generic name for the product |
| 119 | `GENERIC_NAME_KEY` | VARCHAR(100) |  |  | All uppercase generic name for the product. Used for sorting the reports |
| 120 | `GEN_LEDGER_ACCT_CODE` | VARCHAR(50) |  |  | General Ledger Account Code |
| 121 | `GFC_CKI` | VARCHAR(100) |  |  | Cerner Knoweldge Index for generic formulation as defined by Multum. CKI is MUL.FRMLTN! |
| 122 | `GFC_CODE` | VARCHAR(6) |  |  | Generic Formulation Code as defined by Medical Economics (Redbook/Micromedex) - NO LONGER IN ACTIVE USE |
| 123 | `GFC_DESC` | VARCHAR(255) |  |  | Description for Generic Formulation |
| 124 | `INFUSE_OVER` | DOUBLE |  |  | Determines how long to infuse an IV |
| 125 | `INFUSE_OVER_UNIT_CD` | DOUBLE | NOT NULL |  | Unit of measure for Infuse over |
| 126 | `ING_SENT_ID` | DOUBLE | NOT NULL |  | Not in use. |
| 127 | `INTERMITTENT_FILTER_IND` | DOUBLE |  |  | Used to indicate product should appear on product selection lists including intermittent order products |
| 128 | `ITEM_ID` | DOUBLE | NOT NULL |  | Primary Key - Item id for the product |
| 129 | `J_CODE` | VARCHAR(25) |  |  | Not in use. |
| 130 | `LABEL_DESC` | VARCHAR(100) |  |  | Label description for the product. |
| 131 | `LABEL_DESC_KEY` | VARCHAR(100) |  |  | All upper case label description. |
| 132 | `LEGAL_STATUS_CD` | DOUBLE | NOT NULL |  | Legal status assigned by national drug regulatory agencies. (DEA, etc.) |
| 133 | `LOC_CD1` | DOUBLE |  |  | Location_cd from code set 220. |
| 134 | `LOC_CD10` | DOUBLE |  |  | Location_cd from code set 220. |
| 135 | `LOC_CD11` | DOUBLE |  |  | Location_cd from code set 220. |
| 136 | `LOC_CD12` | DOUBLE |  |  | Location_cd from code set 220. |
| 137 | `LOC_CD13` | DOUBLE |  |  | Location_cd from code set 220. |
| 138 | `LOC_CD14` | DOUBLE |  |  | Location_cd from code set 220. |
| 139 | `LOC_CD15` | DOUBLE |  |  | Location_cd from code set 220. |
| 140 | `LOC_CD16` | DOUBLE |  |  | Location_cd from code set 220. |
| 141 | `LOC_CD17` | DOUBLE |  |  | Location_cd from code set 220. |
| 142 | `LOC_CD18` | DOUBLE |  |  | Location_cd from code set 220. |
| 143 | `LOC_CD19` | DOUBLE |  |  | Location_cd from code set 220. |
| 144 | `LOC_CD2` | DOUBLE |  |  | Location_cd from code set 220. |
| 145 | `LOC_CD20` | DOUBLE |  |  | Location_cd from code set 220. |
| 146 | `LOC_CD21` | DOUBLE |  |  | Location_cd from code set 220. |
| 147 | `LOC_CD22` | DOUBLE |  |  | Location_cd from code set 220. |
| 148 | `LOC_CD23` | DOUBLE |  |  | Location_cd from code set 220. |
| 149 | `LOC_CD24` | DOUBLE |  |  | Location_cd from code set 220. |
| 150 | `LOC_CD25` | DOUBLE |  |  | Location_cd from code set 220. |
| 151 | `LOC_CD26` | DOUBLE |  |  | Location_cd from code set 220. |
| 152 | `LOC_CD27` | DOUBLE |  |  | Location_cd from code set 220. |
| 153 | `LOC_CD28` | DOUBLE |  |  | Location_cd from code set 220. |
| 154 | `LOC_CD29` | DOUBLE |  |  | Location_cd from code set 220. |
| 155 | `LOC_CD3` | DOUBLE |  |  | Location_cd from code set 220. |
| 156 | `LOC_CD30` | DOUBLE |  |  | Location_cd from code set 220. |
| 157 | `LOC_CD4` | DOUBLE |  |  | Location_cd from code set 220. |
| 158 | `LOC_CD5` | DOUBLE |  |  | Location_cd from code set 220. |
| 159 | `LOC_CD6` | DOUBLE |  |  | Location_cd from code set 220. |
| 160 | `LOC_CD7` | DOUBLE |  |  | Location_cd from code set 220. |
| 161 | `LOC_CD8` | DOUBLE |  |  | Location_cd from code set 220. |
| 162 | `LOC_CD9` | DOUBLE |  |  | Location_cd from code set 220. |
| 163 | `MANF_IDENTIFIER_BRAND` | VARCHAR(100) |  |  | Brand Name identifier for manufacturer item |
| 164 | `MANF_IDENTIFIER_DESC` | VARCHAR(100) |  |  | Label description for manufacturer item for this product |
| 165 | `MANF_IDENTIFIER_GENERIC` | VARCHAR(100) |  |  | Generic Name for manufacturer item associated with this product |
| 166 | `MANF_IDENTIFIER_MNEMONIC` | VARCHAR(100) |  |  | Order entry mnemonic for manufacturer_item associated with this product |
| 167 | `MANF_IDENTIFIER_PYXIS` | VARCHAR(100) |  |  | PYXIS interface ID for manufacturer_item associated with this product |
| 168 | `MANF_IDENTIFIER_UB92` | VARCHAR(100) |  |  | UB92 classification code for manufacturer_item associated with this item |
| 169 | `MANF_ITEM_ID` | DOUBLE | NOT NULL |  | Item_ID for manufacturer_item associated with this product |
| 170 | `MANF_STATUS` | DOUBLE |  |  | Is manufacturer_item active |
| 171 | `MANUFACTURER_CD` | DOUBLE | NOT NULL |  | Manufacturer for given product/NDC |
| 172 | `MAX_PAR_SUPPLY` | DOUBLE |  |  | Maximum number of doses to be dispensed in a 24hr period for PRN orders |
| 173 | `MDX_GFC_NOMEN_ID` | DOUBLE | NOT NULL |  | Nomenclature id assigned to the Micromedex generic formulation code for this product. |
| 174 | `MED_FILTER_IND` | DOUBLE |  |  | Used to indicate product should appear on product selection lists including medication order products |
| 175 | `MED_TYPE_FLAG` | DOUBLE |  |  | Flag to indicate the type of order |
| 176 | `MEQ_FACTOR` | DOUBLE |  |  | Factor for determininig ratio for ml equivalents |
| 177 | `MMOL_FACTOR` | DOUBLE |  |  | Factor for ratio to milliimoles |
| 178 | `MNEMONIC` | VARCHAR(50) |  |  | Order entry mnemonic for product |
| 179 | `NDC` | VARCHAR(13) | NOT NULL |  | National Drug Code (US FDA) identifier |
| 180 | `NDC_ACTIVE_IND` | DOUBLE |  |  | Is NDC active for product |
| 181 | `NON_RB_IND` | DOUBLE |  |  | IS item in reference database |
| 182 | `OE_FORMAT_FLAG` | DOUBLE |  |  | Default order Entry Format to display for this product |
| 183 | `OE_FORMAT_ID` | DOUBLE | NOT NULL |  | Order Entry Format for this type of order |
| 184 | `ORDER_ALERT1_CD` | DOUBLE | NOT NULL |  | First order alert for the product |
| 185 | `ORDER_ALERT2_CD` | DOUBLE | NOT NULL |  | Second order alert for the product |
| 186 | `ORD_SENT_ID` | DOUBLE | NOT NULL |  | Order Sentence associated with the product |
| 187 | `OS_DISPLAY_LINE` | VARCHAR(255) |  |  | Denormalized order_sentence display line. |
| 188 | `OUTER_QTY` | DOUBLE |  |  | Outer package quantity from package_type. |
| 189 | `OUTER_UOM` | DOUBLE |  |  | Unit of measure for outer package quantity from code set 54 |
| 190 | `PRICE_SCHEDULE_ID` | DOUBLE | NOT NULL |  | Price schedule ID used for billing |
| 191 | `PRICE_SCHED_SHORT_DESC` | VARCHAR(50) |  |  | Text description for price_scjhedule |
| 192 | `PRIMARY_IND` | DOUBLE |  |  | Indicates whether this item_id/ndc combination is the primary choice for dispensing |
| 193 | `PRIMARY_MNEMONIC` | VARCHAR(100) |  |  | Primary Mnemonic used for PowerChart order entry |
| 194 | `PRN_IND` | DOUBLE |  |  | Scheduled/PRN indicator - derived from def_prn_val |
| 195 | `PROD_ACTIVE_IND` | DOUBLE |  |  | IS product acvtive in formulary |
| 196 | `PYXIS` | VARCHAR(30) |  |  | PYXIS interface ID for product. |
| 197 | `QTY` | DOUBLE |  |  | Dispense Quantity |
| 198 | `REF_DOSE` | VARCHAR(25) |  |  | Reference dose, a string value, combination of strength/strength unit and volume/volume unit. Shows up in Given Strength field. |
| 199 | `REUSABLE_IND` | DOUBLE |  |  | Indicates whether this product can be re-used when returned to the pharmacy for credit. |
| 200 | `RX_DEVICE1` | VARCHAR(100) |  |  | Device code from code set 11000. |
| 201 | `RX_DEVICE2` | VARCHAR(100) |  |  | Device code from code set 11000. |
| 202 | `RX_DEVICE3` | VARCHAR(100) |  |  | Device code from code set 11000. |
| 203 | `RX_DEVICE4` | VARCHAR(100) |  |  | Device code from code set 11000. |
| 204 | `RX_DEVICE5` | VARCHAR(100) |  |  | Device code value from code set 11000. |
| 205 | `RX_MISC1` | VARCHAR(100) |  |  | CDF meaning for rx_device1, from code set 11000 |
| 206 | `RX_MISC2` | VARCHAR(100) |  |  | CDF meaning for rx_device2, from code set 11000 |
| 207 | `RX_MISC3` | VARCHAR(100) |  |  | CDF meaning for rx_device3, from code set 11000 |
| 208 | `RX_MISC4` | VARCHAR(100) |  |  | CDF meaning for rx_device4, from code set 11000 |
| 209 | `RX_MISC5` | VARCHAR(100) |  |  | CDF meaning for rx_device5, from code set 11000 |
| 210 | `RX_MNEMONIC` | VARCHAR(255) |  |  | Pharmacy mnemonic for this product |
| 211 | `SEQUENCE` | DOUBLE | NOT NULL |  | Internal indicator for set items. |
| 212 | `SIDE_EFFECT_CODE` | VARCHAR(10) |  |  | SIde effect code for adverse reaction charting |
| 213 | `STRENGTH` | DOUBLE |  |  | Given Strength for the product |
| 214 | `STRENGTH_UNIT_CD` | DOUBLE | NOT NULL |  | Given strength units for the product |
| 215 | `SYNONYM_ID` | DOUBLE | NOT NULL |  | The synonym_id for the rx_mnemonic |
| 216 | `TEST` | DOUBLE |  |  | Not in use. |
| 217 | `UB92` | VARCHAR(30) |  |  | UB92 classification for product |
| 218 | `UOM_CD` | DOUBLE | NOT NULL |  | The unit of measure for the dispense qty |
| 219 | `USED_AS_BASE_IND` | DOUBLE |  |  | Indicates that this product can be used as a base solution for a multi ingredient order |
| 220 | `VALID_IV_IND` | DOUBLE |  |  | Indicates that this item can be used in an IV order |
| 221 | `VOLUME` | DOUBLE |  |  | Given Volume for the product |
| 222 | `VOLUME_UNIT_CD` | DOUBLE | NOT NULL |  | Units of measure for the given volume |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

