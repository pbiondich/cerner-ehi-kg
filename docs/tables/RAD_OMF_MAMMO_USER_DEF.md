# RAD_OMF_MAMMO_USER_DEF

> Rad OMF Mammo User Defined

**Description:** This table holds abstract field for use with Mammo PV user defined fields.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `CD_COLUMN` | VARCHAR(50) | NOT NULL |  | This is a unique identifier for the mammography follow up fields. It corresponds to the Cerner_meaning_str column on rad_omf_mammo_details and rad_omf_mammo_find_details. |
| 3 | `DISP_COLUMN` | VARCHAR(50) | NOT NULL |  | This is the description that displays for a field. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `FACT_IND` | DOUBLE | NOT NULL |  | This is an indicator signifying whether or not a field is a FACT. |
| 6 | `INDICATOR_CD` | DOUBLE | NOT NULL |  | This is the foreign key to the omf_indicator table. |
| 7 | `OMF_FACT_IND` | DOUBLE |  |  | This is an indicator signifying whether or not a field is a fact. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

