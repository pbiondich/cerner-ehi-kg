# SURGICAL_STAFF_AVAILABILITY

> Identifies the detailed availability of surgical staff

**Description:** Surgical Staff Availability  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADD_ON_IND` | DOUBLE | NOT NULL |  | Identifies the staff availability row as loaded from a foreign system (0) or added from within Surginet (1). Default = 0 |
| 6 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context number from the record info block. |
| 7 | `CREATE_DT_TM` | DATETIME |  |  | The date and time the record was created |
| 8 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The personnel ID of the person who created the row in the table |
| 9 | `CREATE_TASK` | DOUBLE |  |  | The registered (assigned) task number for the process that inserted the row. |
| 10 | `END_DT_TM` | DATETIME | NOT NULL |  | The date and time for which a specific personnel is scheduled to end work. |
| 11 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the PRSNL table. It is an internal system assigned number. |
| 12 | `START_DT_TM` | DATETIME | NOT NULL |  | The date and time for which a specific personnel is scheduled to start work. |
| 13 | `SURGICAL_STAFF_AVAILABILITY_ID` | DOUBLE | NOT NULL |  | unique sequence number for this table |
| 14 | `SURG_AREA_CD` | DOUBLE | NOT NULL |  | Surgical area the staff personnel is associated with. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

