# LH_CQM_MEAS_SVC_ENTITY_R

> Relates the measure to the entity that the measure applies to, i.e. a hospital or eligible provider.

**Description:** Lighthouse Clinical Quality Measures Service Entity Relation  
**Table type:** REFERENCE  
**Primary key:** `LH_CQM_MEAS_SVC_ENTITY_R_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 4 | `LH_CQM_MEAS_ID` | DOUBLE | NOT NULL |  | The measure that is being related to this service entity. |
| 5 | `LH_CQM_MEAS_SVC_ENTITY_R_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the LH_CQM_MEAS_SVC_ENTITY_R table. |
| 6 | `LH_CQM_REPORT_TYPE_TFLG` | VARCHAR(5) |  |  | Determines the reporting type as MIPs or MVPs. |
| 7 | `ORIG_LH_CQM_MEAS_SVCENT_R_ID` | DOUBLE | NOT NULL | FK→ | Used for versioning. Contains the value of the PK for a particular set of rows in LH_CQM_MEAS_SVC_ENTITY_R. |
| 8 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifies the Eligible Provider or Hospital that is being related to this measure. |
| 9 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | A pointer to the table that holds the service entity being related to this measure. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORIG_LH_CQM_MEAS_SVCENT_R_ID` | [LH_CQM_MEAS_SVC_ENTITY_R](LH_CQM_MEAS_SVC_ENTITY_R.md) | `LH_CQM_MEAS_SVC_ENTITY_R_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [LH_CQM_MEAS_SVC_ENTITY_R](LH_CQM_MEAS_SVC_ENTITY_R.md) | `ORIG_LH_CQM_MEAS_SVCENT_R_ID` |

