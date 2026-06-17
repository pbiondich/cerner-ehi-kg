# DISPENSE_CATEGORY

> Child table for codeset 4008. Contains information for dispense categories

**Description:** DISPENSE CATEGORY  
**Table type:** REFERENCE  
**Primary key:** `DISPENSE_CATEGORY_CD`  
**Columns:** 52  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AUTO_CREDIT_IND` | DOUBLE | NOT NULL |  | Indicates if auto crediting should be performed on scheduled administration charge doses. |
| 2 | `CHARGE_ON_SCHED_ADMIN_IND` | DOUBLE | NOT NULL |  | Indicates if charges for a dispense should be based on the scheduled administration date for a particular dose. |
| 3 | `CHARGE_PT_PRN_IND` | DOUBLE |  |  | PRN orders' charge creation point.0 = Manual, 1 = charge on dispense, 2 = charge on administration |
| 4 | `CHARGE_PT_SCH_IND` | DOUBLE |  |  | Scheduled orders' charge creation point.0 = Manual, 1 = charge on dispense, 2 = charge on administration |
| 5 | `DENIAL_REPORT_FORMAT_CD` | DOUBLE | NOT NULL |  | The report format for the Patient Denial Report |
| 6 | `DISPENSE_CATEGORY_CD` | DOUBLE | NOT NULL | PK FK→ | Dispense Category Code |
| 7 | `DISP_FILL_DAYS_SUPPLY_AMT` | DOUBLE | NOT NULL |  | Indicates Fill Batch dispensing Days Supply amount. |
| 8 | `DISP_FILL_DAYS_SUPPLY_IND` | DOUBLE | NOT NULL |  | Indicates that the Fill Batch dispensing method is 'Days Supply'. |
| 9 | `DISP_FILL_DAYS_SUP_PKG_IND` | DOUBLE | NOT NULL |  | Indicates if days supply with full package dispensing is being used for fill lists. |
| 10 | `DISP_FILL_LBL_PRINTING_FLAG` | DOUBLE | NOT NULL |  | Indicates how the system generates label and fill list printing data during continuing dose processing and is being added to address potential database and performance issues for sites running long fills. 0 = per dose; 1 = per dispense; 2 = per package. |
| 11 | `DISP_FILL_PROD_PKG_IND` | DOUBLE | NOT NULL |  | Indicates that the Fill Batch dispensing method is 'Package Supply'. |
| 12 | `DISP_FILL_QTY_IND` | DOUBLE |  |  | Indicator for how fill-processing should determine number of doses to dispense. e.g.: for bulk orders, fill quantity would likely be 1 or 0. -1 = Calculate the number of fill doses to dispense by frequency schedule or PAR value. 0-9 = Default as the number of fill doses to dispense. |
| 13 | `DISP_FROM_PHLOCN_IND` | DOUBLE |  |  | Always dispense an order with this dispense category from a pharmacy location if true. |
| 14 | `DISP_QTY_RATIO_IND` | DOUBLE |  |  | Indicates whether the ratio between the dose and the units to be dispensed should be automatically maintained by the system. NOTE: when maintaining the ratio, the round_disp_qty_ind may cause the units to be dispensed to round up to the next whole unit, i.e. cause the ratio to be different for fractional doses. 0 - Don't maintain the str/vol/dose ratio 1 - Maintain the str/vol/dose ratio |
| 15 | `FILL_LIST_FORMAT_CD` | DOUBLE | NOT NULL |  | Format cd associated with batch dispensing. Initial labels will use a separate format as well. |
| 16 | `INDIVIDUAL_DOSE_DISPENSING_IND` | DOUBLE | NOT NULL |  | Indicates whether or not the dispense event will generate separate events for each dose. 0 - do not do individual dispensing, 1 - do individual dispensing. |
| 17 | `INTERIM_DAYS_SUPPLY_AMT` | DOUBLE | NOT NULL |  | Indicates Interim Dose dispensing Days Supply amount. |
| 18 | `INTERIM_DAYS_SUPPLY_IND` | DOUBLE | NOT NULL |  | Indicates that the Interim Dose dispensing method is 'Days Supply'. |
| 19 | `INTERIM_DAYS_SUP_PKG_IND` | DOUBLE | NOT NULL |  | Indicates if days supply with full package dispensing is being used |
| 20 | `INTERIM_DISP_QTY_IND` | DOUBLE |  |  | Indicator for how order-entry processing should determine number of doses to dispense initially (interim doses). e.g.: for Bulk orders, initial doses might always be 1. -1 = Calculate the number of interim doses to dispense.0-9 = Default as the number of interim doses to dispense. Note: "0" means "do not calculate interim doses." |
| 21 | `INTERIM_LBL_PRINTING_FLAG` | DOUBLE | NOT NULL |  | Indicates how the system generates label printing data during initial dose processing and is being added to address potential database and performance issues for sites running long fills. |
| 22 | `INTERIM_PROD_PKG_IND` | DOUBLE | NOT NULL |  | Indicates that the Interim Dose dispensing method is 'Package Supply'. |
| 23 | `LABEL_FORMAT_CD` | DOUBLE | NOT NULL | FK→ | This column contains the code value for the label format associated with the dispense category |
| 24 | `LAST_RESORT_FILL_HRS` | DOUBLE |  |  | Number of hours for which to calculate initial doses needing to be sent, if this type is NOT on a fill list for the nursing unit ordering the medication order. Non-negative integer. |
| 25 | `LAST_RESORT_FILL_TIME` | DOUBLE |  |  | The time of day used for calculating initial doses needing to be sent, if this type is NOT on a fill list for the nursing unit ordering the medication order. Non-negative integers expressed in minutes that must be converted to the time of day. |
| 26 | `LBL_PER_DOSE` | DOUBLE |  |  | Indicates whether a label should be printed for each dose time or only 1 label per order - NOT IN USE |
| 27 | `LEAFLET_FORMAT_CD` | DOUBLE | NOT NULL |  | Leaflet format cd |
| 28 | `ORDER_TYPE_FLAG` | DOUBLE |  |  | Determines the type of order entry format used with this dispense category |
| 29 | `PHARM_TYPE_CD` | DOUBLE | NOT NULL |  | Pharmacy type cd |
| 30 | `PREVIEW_FORMAT_CD` | DOUBLE |  |  | The custom label program used to generate the Postscript output for the Pharmacy Print Preview functionality. |
| 31 | `PRICE_SCHED_ID` | DOUBLE | NOT NULL | FK→ | Price Schedule Id associated with the category |
| 32 | `REFILL_NOTIFY_FORMAT_CD` | DOUBLE | NOT NULL |  | Contains the format code for the refill notification. |
| 33 | `REPLACE_EVERY` | DOUBLE |  |  | Defines a default replace every for an IV order. This field is only used if the interval is > than this field. |
| 34 | `REPORT_FORMAT_CD` | DOUBLE | NOT NULL |  | This column contains the code value for the report format associated with the dispense category. |
| 35 | `ROUND_DISP_QTY_IND` | DOUBLE |  |  | Indicates if the quantity to be dispensed can be fractional or if the system should force it to be rounded to the nearest whole number. 0 = Allow partial units to be dispensed e.g. default 100MG 1EA, ordered as 150MG yields 1.5EA.1 = Round up units to be dispensed to the nearest whole number when the strength/volume entered does not yield a whole dispense unit, e.g. default 100MG 1EA, ordered as 150MG yields 2EA. |
| 36 | `SKIP_DISPENSE_FLAG` | DOUBLE | NOT NULL |  | Indicates whether this dispense category supports skipping of certain products, from dispensing, in a multi-ingredient IV/Continuous order. |
| 37 | `TEMP_STOCK_IND` | DOUBLE | NOT NULL |  | Indicator that the dispense category is defined as a temporary stock dispense category. |
| 38 | `TPN_IND` | DOUBLE |  |  | Indicator that dispense category is defined as a TPN dispense category |
| 39 | `UNSUPPORTED_DAYS_SUPPLY_AMT` | DOUBLE | NOT NULL |  | Indicates the Days Supply amount when the dispensing method for a patient's location that is unsupported by a Fill Batch process is 'Days Supply'. |
| 40 | `UNSUPPORTED_DAYS_SUPPLY_IND` | DOUBLE | NOT NULL |  | Indicates that the dispensing method for a patient's location that is unsupported by a Fill Batch process, will be 'Days Supply'. |
| 41 | `UNSUPPORTED_DAYS_SUP_PKG_IND` | DOUBLE | NOT NULL |  | Indicates if days supply with full package dispensing is being used for continuing dispensing when not on a fill. |
| 42 | `UNSUPPORTED_DOSES_AMT` | DOUBLE | NOT NULL |  | Indicates the Doses to be dispensed when the dispensing method for a patient's location that is unsupported by a Fill Batch process is "Specified Doses'. |
| 43 | `UNSUPPORTED_DOSES_IND` | DOUBLE | NOT NULL |  | Indicates that the dispensing method for a patient's location that is unsupported by a Fill Batch process, will be a 'Specified Doses. |
| 44 | `UNSUPPORTED_LBL_PRINTING_FLAG` | DOUBLE | NOT NULL |  | Indicates how the system generates label printing data during on-demand dose processing and is being added to address potential database and performance issues for sites filling large quantities at a time.012 |
| 45 | `UNSUPPORTED_PROD_PKG_IND` | DOUBLE | NOT NULL |  | Indicates that the dispensing method for a patient's location that is unsupported by a Fill Batch process, will be 'Package Supply'. |
| 46 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 49 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 50 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 51 | `VALIDATION_FORMAT_CD` | DOUBLE | NOT NULL |  | Validation format cd |
| 52 | `WORKFLOW_CD` | DOUBLE | NOT NULL |  | The dispense sequence associated to the product which is used to route orders to the dispense monitor. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPENSE_CATEGORY_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `LABEL_FORMAT_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `PRICE_SCHED_ID` | [PRICE_SCHED](PRICE_SCHED.md) | `PRICE_SCHED_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DISPENSE_CATEGORY_FORM_R](DISPENSE_CATEGORY_FORM_R.md) | `DISPENSE_CATEGORY_CD` |
| [RXS_WORKLIST_DISP_CAT_R](RXS_WORKLIST_DISP_CAT_R.md) | `DISPENSE_CATEGORY_CD` |

