# ORDER_STAGING

> This table store orders staging data

**Description:** Orders_Staging  
**Table type:** ACTIVITY  
**Primary key:** `ORDER_STAGING_ID`  
**Columns:** 15  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CHARTED_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Identifier of a charted order id |
| 2 | `CLIENT_IDENT` | VARCHAR(255) | NOT NULL |  | Client appication Identifier which inserted this row. |
| 3 | `DATA_BLOB` | LONGBLOB |  |  |  |
| 4 | `ENCOUNTER_ID` | DOUBLE | NOT NULL | FK→ | Encounter id for the patient encounter |
| 5 | `ORDER_STAGING_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Identifier of a person / patient |
| 7 | `STAGING_STATUS_TXT` | VARCHAR(20) | NOT NULL |  | The staging status of the medication order. |
| 8 | `START_DT_TM` | DATETIME |  |  | Start Date Time of a medication |
| 9 | `STATUS_TXT` | VARCHAR(20) | NOT NULL |  | The status of the medication order. |
| 10 | `STOP_DT_TM` | DATETIME |  |  | Stop date time of a medication |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CHARTED_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `ENCOUNTER_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [ORDER_STAGING_ERX_INFO](ORDER_STAGING_ERX_INFO.md) | `ORDER_STAGING_ID` |
| [ORDER_STAGING_EXT_IDENT](ORDER_STAGING_EXT_IDENT.md) | `ORDER_STAGING_ID` |

