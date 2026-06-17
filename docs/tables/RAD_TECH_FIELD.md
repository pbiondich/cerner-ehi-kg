# RAD_TECH_FIELD

> The Rad_Tech_Field table holds individual radiology technical comments fields

**Description:** Radiology Technical Comment Fields  
**Table type:** REFERENCE  
**Primary key:** `FIELD_ID`  
**Columns:** 12  
**Referenced by:** 8 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `FIELD_DESC` | VARCHAR(60) | NOT NULL |  | The field description names a radiology technical comment field. |
| 6 | `FIELD_ID` | DOUBLE | NOT NULL | PK | The Field_Id uniquely identifies a row in the Rad_Tech_Field table. It serves no other purpose other than to uniquely identify the row . |
| 7 | `FIELD_TYPE_FLAG` | DOUBLE | NOT NULL |  | The field type flags defines the type of a field. 0 = Header, 1 = Number, 2 = Text, 3 = Date, 4 = Single Choice, 5 = Multi Choice |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (8)

| From table | Column |
|------------|--------|
| [RAD_OMF_TC_INDICATOR](RAD_OMF_TC_INDICATOR.md) | `FIELD_ID` |
| [RAD_OMF_TC_IND_R](RAD_OMF_TC_IND_R.md) | `PARENT_FIELD_ID` |
| [RAD_TECH_CMT_DATA](RAD_TECH_CMT_DATA.md) | `FIELD_ID` |
| [RAD_TECH_CMT_DATA](RAD_TECH_CMT_DATA.md) | `PARENT_FIELD_ID` |
| [RAD_TECH_CMT_DATA_HIST](RAD_TECH_CMT_DATA_HIST.md) | `FIELD_ID` |
| [RAD_TECH_CMT_DATA_HIST](RAD_TECH_CMT_DATA_HIST.md) | `PARENT_FIELD_ID` |
| [RAD_TECH_FLD_FMT_R](RAD_TECH_FLD_FMT_R.md) | `FIELD_ID` |
| [RAD_TECH_FLD_FMT_R](RAD_TECH_FLD_FMT_R.md) | `PARENT_FIELD_ID` |

