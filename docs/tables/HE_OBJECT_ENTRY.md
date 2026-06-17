# HE_OBJECT_ENTRY

> Store ENTRIES for serialized health expert objects for future reuse. These object will include knowledge base versions, resolved fact patterns, and other objects used to optimize processing by the health expert jobs.

**Description:** HE_OBJECT_ENTRY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ENTRY_NAME` | VARCHAR(250) | NOT NULL |  | Uniquely identifies this entry by a name. Each entry may have only one row. |
| 2 | `FULL_ENTRY_NAME` | LONGTEXT |  |  | This column will be storing the keys for the fact pattern resolver cache, a key could be event set name, order catalog mnemonic, source string or identifier or concept CKI and source vocabulary for nomenclatures |
| 3 | `HE_OBJECT_ENTRY_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 4 | `HE_OBJECT_ID` | DOUBLE | NOT NULL | FK→ | Unique identifier of the health expert object name that this entry is saved under. |
| 5 | `LONG_BLOB_ID` | DOUBLE | NOT NULL | FK→ | Reference to the long blob where then contents of the entry are serialized. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `HE_OBJECT_ID` | [HE_OBJECT](HE_OBJECT.md) | `HE_OBJECT_ID` |
| `LONG_BLOB_ID` | [LONG_BLOB](LONG_BLOB.md) | `LONG_BLOB_ID` |

