# PRSNL_OUT_OF_OFFICE_DIST

> This table stores how work items are distributed for an Out-of-Office Event.

**Description:** Personnel Out of Office Distribution  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `DISTRIBUTE_TO_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Contains the ID of the personnel to which a work item is distributed. |
| 4 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 5 | `ORIG_OUT_OF_OFFICE_DIST_ID` | DOUBLE | NOT NULL |  | Used to track versions of the personnel out of office group information. This field will always point back to the initial value created. This may be used to find the correct version when combined with begin and end effective dates and times. |
| 6 | `PFT_WORKFLOW_STATUS_CD` | DOUBLE | NOT NULL |  | The status code representing the related workflow. |
| 7 | `PRSNL_OUT_OF_OFFICE_DIST_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the PRSNL_OUT_OF_OFFICE_DIST table. |
| 8 | `PRSNL_OUT_OF_OFFICE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related Out of Office Event. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISTRIBUTE_TO_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PRSNL_OUT_OF_OFFICE_ID` | [PRSNL_OUT_OF_OFFICE](PRSNL_OUT_OF_OFFICE.md) | `PRSNL_OUT_OF_OFFICE_ID` |

