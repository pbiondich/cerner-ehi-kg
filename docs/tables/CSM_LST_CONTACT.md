# CSM_LST_CONTACT

> lists the last contact made for each phone id that comes through the CSM system

**Description:** CSM LST CONTACT  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CONTACT` | VARCHAR(100) |  |  | free textname for the contact |
| 3 | `CSM_CONTACT_ID` | DOUBLE | NOT NULL |  | Not used, can't remove for packets |
| 4 | `CSM_LST_DT_TM` | DATETIME | NOT NULL |  | date and time of last contact |
| 5 | `CSM_LST_REC_ID` | DOUBLE | NOT NULL |  | unique record identifier |
| 6 | `CSM_PHONE_STAT_ID` | DOUBLE | NOT NULL | FK→ | unique identifier for the phone status during the last contact attempt |
| 7 | `CSM_REQ_ID` | DOUBLE |  | FK→ | Uniquely identifies the related request. |
| 8 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 9 | `PHONE_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of a phone number |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CSM_PHONE_STAT_ID` | [CSM_PHONE_STATS](CSM_PHONE_STATS.md) | `CSM_PHONE_STAT_ID` |
| `CSM_REQ_ID` | [CSM_REQUESTS](CSM_REQUESTS.md) | `CSM_REQ_ID` |
| `PERSON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PHONE_ID` | [PHONE](PHONE.md) | `PHONE_ID` |

