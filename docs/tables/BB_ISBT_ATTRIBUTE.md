# BB_ISBT_ATTRIBUTE

> Cerner defined table that matches various ISBT records

**Description:** BLOOD BANK ISBT ATTRIBUTE  
**Table type:** REFERENCE  
**Primary key:** `BB_ISBT_ATTRIBUTE_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ATTRIBUTE_GROUP` | VARCHAR(40) | NOT NULL |  | Each ISBT attribute is part of an attribute group. When printing an ISBT label, the attribute group determines which order the label prints in. This field would act like a cdf_meaning field. It could be hard coded in the program. |
| 6 | `BB_ISBT_ATTRIBUTE_ID` | DOUBLE | NOT NULL | PK | Unique number to keep each record unique. |
| 7 | `LABEL_DISPLAY` | VARCHAR(40) | NOT NULL |  | Each ISBT attribute will be displayed on the ISBT label. This field will be the text that gets displayed on the label. |
| 8 | `STANDARD_DISPLAY` | VARCHAR(40) | NOT NULL |  | This field should match exactly to what is in the ICCBBA ISBT database. This field acts like a cdf_meaning and can be hard coded. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [BB_ISBT_ATTRIBUTE_R](BB_ISBT_ATTRIBUTE_R.md) | `BB_ISBT_ATTRIBUTE_ID` |

