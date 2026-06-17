# MED_ADMIN_RECORD

> Table used to maintain medication administration records.

**Description:** Medication Administrations  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMIN_BLOB` | LONGBLOB |  |  | BLOB containing a representation of medication administration record data. |
| 2 | `BLOB_DEF_VERSION` | DOUBLE | NOT NULL |  | The version of the medication administration definition stored in the ADMINS_BLOB. |
| 3 | `EARLIEST_START_DT_TM` | DATETIME |  |  | The date and time the earliest administration was started. |
| 4 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single person in the ENCOUNTER table. |
| 5 | `LATEST_COMPLETED_DT_TM` | DATETIME |  |  | The date and time corresponding to the administration with the latest completion date. |
| 6 | `MED_ADMIN_RECORD_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 7 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single order in the ORDERS table. |
| 8 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single person in the PERSON table. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

