# PERSON_COMBINE_BATCH

> The person_combine_batch table is used for the batch Person combine process. It is populated from HNACombine.exe

**Description:** Person Combine Batch  
**Table type:** ACTIVITY  
**Primary key:** `PERSON_COMBINE_BATCH_ID`  
**Columns:** 21  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BATCH_DT_TM` | DATETIME |  |  | Date the batrch record is scheduled to be processed. |
| 6 | `BATCH_STATUS_CD` | DOUBLE | NOT NULL |  | Contains the value of the status of the batch. |
| 7 | `CREATE_DT_TM` | DATETIME |  |  | This is the date and time that the row was created. |
| 8 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The person responsible for inserting this row on the table |
| 9 | `FROM_PERSON_ID` | DOUBLE | NOT NULL | FK→ | FROM_PERSON_ID, this id gets combined into the TO_PERSON_ID |
| 10 | `OWNER_NAME` | VARCHAR(255) |  |  | Name of the process that owns the row. |
| 11 | `PERSON_COMBINE_BATCH_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the person_combine_batch. |
| 12 | `PERSON_COMBINE_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related person combine row. |
| 13 | `PERSON_MATCHES_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related person_matches row. |
| 14 | `PROCESSED_DT_TM` | DATETIME |  |  | The date the batch record was actually processed. |
| 15 | `REVERSE_COMBINE_IND` | DOUBLE |  |  | Indicator for Reverse Combine mode. |
| 16 | `TO_PERSON_ID` | DOUBLE | NOT NULL | FK→ | TO_PERSON_ID surviving person that gets data from the FROM_PERSON_ID |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `FROM_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PERSON_COMBINE_ID` | [PERSON_COMBINE](PERSON_COMBINE.md) | `PERSON_COMBINE_ID` |
| `PERSON_MATCHES_ID` | [PERSON_MATCHES](PERSON_MATCHES.md) | `PERSON_MATCHES_ID` |
| `TO_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [EMPI_IMPORT_MATCH](EMPI_IMPORT_MATCH.md) | `PERSON_COMBINE_BATCH_ID` |

