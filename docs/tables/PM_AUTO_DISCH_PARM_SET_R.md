# PM_AUTO_DISCH_PARM_SET_R

> The PM_AUTO_DISCH_PARM_SET_RELTN table stores information about the relationships between parameter sets and auto discharge criteria.

**Description:** Patient Management Auto Discharge Parameter Set Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 18

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Contains the row creation date. |
| 7 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | Contains the id of the person who created the row. |
| 8 | `ENCNTR_TYPE_CD` | DOUBLE | NOT NULL |  | Categorizes the encounter into a logical group or type. Examples may include inpatient, outpatient, etc. |
| 9 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 10 | `LOC_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | Patient location with a location type of facility. |
| 11 | `LOC_NURSE_UNIT_CD` | DOUBLE | NOT NULL | FK→ | Patient location with a location type of nurse unit. |
| 12 | `PM_AUTO_DISCH_PARM_SET_R_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the PM_AUTO_DISCH_PARM_SET_RELTN table. |
| 13 | `RC_PARAMETER_SET_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the RC_PARAMETER_SET table. It is an internal system assigned number. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LOC_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOC_NURSE_UNIT_CD` | [NURSE_UNIT](NURSE_UNIT.md) | `LOCATION_CD` |
| `RC_PARAMETER_SET_ID` | [RC_PARAMETER_SET](RC_PARAMETER_SET.md) | `RC_PARAMETER_SET_ID` |

