# DRC_FACILITY_R_VER

> Allow for versioning of DRC_FACILITY_R

**Description:** Dose Range Check to Facility Relation table - Versioning Table  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `DOSE_RANGE_CHECK_ID` | DOUBLE | NOT NULL | FK→ | FK from DOSE_RANGE_CHECK table. |
| 3 | `DRC_FACILITY_R_ID` | DOUBLE | NOT NULL |  | Primary key |
| 4 | `DRC_GROUP_ID` | DOUBLE | NOT NULL |  | This value comes from MLTM_DRC_GROUP_RELTN.GROUPER_ID |
| 5 | `FACILITY_CD` | DOUBLE | NOT NULL | FK→ | FACILITY CODE. Part of Alternate Key. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VER_SEQ` | DOUBLE | NOT NULL |  | VERSION SEQUENCE Column |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DOSE_RANGE_CHECK_ID` | [DOSE_RANGE_CHECK](DOSE_RANGE_CHECK.md) | `DOSE_RANGE_CHECK_ID` |
| `FACILITY_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

