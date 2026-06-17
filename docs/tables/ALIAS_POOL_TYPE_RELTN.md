# ALIAS_POOL_TYPE_RELTN

> Defines relationships of alias pools to alias types.

**Description:** Alias Pool Type Relationship  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE |  |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE |  |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ALIAS_ENTITY_ALIAS_TYPE_CD` | DOUBLE |  |  | Identifies the type of alias for the given alias_entity_name (e.g. MRN, SSN, HNAMPERSONID, CMRN). |
| 6 | `ALIAS_ENTITY_NAME` | VARCHAR(32) |  |  | The entity name to which this alias pool relationship row is related (i.e. PERSON). |
| 7 | `ALIAS_POOL_CD` | DOUBLE |  | FK→ | Identifies a unique set or list of identifiers (i.e. numbers). The alias pool code also determines the accept/display format for the unique set of identifies. |
| 8 | `ALIAS_POOL_TYPE_RELTN_ID` | DOUBLE | NOT NULL |  | A system generated number used to uniquely identify a row on the ALIAS_POOL_TYPE_RELTN table. |
| 9 | `UPDT_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ALIAS_POOL_CD` | [ALIAS_POOL](ALIAS_POOL.md) | `ALIAS_POOL_CD` |

