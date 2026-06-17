# PREG_BR_CONFIG_HISTORY

> This table will store the historical bedrock configurations for the Partogram Mpage components

**Description:** PREG_BR_CONFIG_HISTORY  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BR_CONFIG_CLOB` | LONGTEXT |  |  | The Historical bedrock settings of an Mpage defined in the profile_type saved as a JSON |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `LOCATION_CD` | DOUBLE | NOT NULL |  | CODE SET:220 - The field identifies the current permanent location of the patient. The location for an inpatient will be valued with the lowest level location type in the hierarchy of facility, building, nurse unit, room, bed |
| 6 | `MP_VIEW_ID` | DOUBLE | NOT NULL | FK→ | Represents the BR_DATAMART_CATEGORY.BR_DATAMART_CATEGORY_ID |
| 7 | `POSITION_CD` | DOUBLE | NOT NULL |  | CODE SET:88; The position is used to determine the applications and tasks the personnel is authorized to use. |
| 8 | `PREG_BR_CONFIG_HISTORY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 9 | `PROFILE_TYPE` | VARCHAR(30) |  |  | The historical Mpage whose settings this row represents |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MP_VIEW_ID` | [BR_DATAMART_CATEGORY](BR_DATAMART_CATEGORY.md) | `BR_DATAMART_CATEGORY_ID` |

