# RAD_OMF_MAMMO

> This is the main summary table for mammo powervision

**Description:** RAD OMF MAMMO  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FOLLOW_UP_PROC_CD` | DOUBLE | NOT NULL |  | This is the mammography follow up procedure code. |
| 2 | `INCLUDE_BREAST_DENSITY_IND` | DOUBLE |  |  | This column will contain value of include breast density statement indicator value, as saved by user in Mammo case maintenance. Possible response values are Yes / No / empty string which is also the default response selected for this question. Planning to store these values as 1 (Yes), 0 (No), NULL (empty string). If this is set to Yes, then the breast density statement set for the selected facility in breast_density_text in Rad_Config_Data table will be printed in mammo notification letters. |
| 3 | `NO_FOL_UP_REQ_IND` | DOUBLE |  |  | If this field is 1, a follow up is not required. If it is 0 or NULL then a follow up is required. |
| 4 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This is the foreign key to the order_radiology table. It uniquely identifies an order. |
| 5 | `RECALL_INTERVAL` | DOUBLE | NOT NULL |  | This is the mammography patient recall interval. |
| 6 | `STAT_CAT_FLAG` | DOUBLE | NOT NULL |  | This flag is used for calculating radiologist performance. |
| 7 | `STUDY_DT_NBR` | DOUBLE |  |  | OMF uses this number to calculate dates. |
| 8 | `STUDY_DT_TM` | DATETIME |  |  | This is the date and time that the study was conducted |
| 9 | `STUDY_ID` | DOUBLE | NOT NULL | FK→ | This is the foreign key to the mammo_study table. |
| 10 | `STUDY_MIN_NBR` | DOUBLE |  |  | OMF uses number to calculate dates. |
| 11 | `STUDY_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `STUDY_ID` | [MAMMO_STUDY](MAMMO_STUDY.md) | `STUDY_ID` |

