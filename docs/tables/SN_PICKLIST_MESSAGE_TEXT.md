# SN_PICKLIST_MESSAGE_TEXT

> Contains message text for surgical picklist and picklist item messages

**Description:** Surginet Picklist Message Text  
**Table type:** ACTIVITY  
**Primary key:** `SN_PICKLIST_MESSAGE_TEXT_ID`  
**Columns:** 13  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME |  |  | Indicates when the message was created |
| 2 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel id of the user who created the message |
| 3 | `LAST_MODIFIED_DT_TM` | DATETIME |  |  | Indicates when the message was last modified |
| 4 | `LAST_MODIFIED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel id of the user who last modified the message |
| 5 | `MESSAGE_TXT` | VARCHAR(4000) | NOT NULL |  | The text of the message |
| 6 | `PARENT_MESSAGE_TEXT_ID` | DOUBLE | NOT NULL | FK→ |  |
| 7 | `SN_PICKLIST_MESSAGE_ID` | DOUBLE | NOT NULL | FK→ | Contains the identifier for the message for this message text |
| 8 | `SN_PICKLIST_MESSAGE_TEXT_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LAST_MODIFIED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `PARENT_MESSAGE_TEXT_ID` | [SN_PICKLIST_MESSAGE_TEXT](SN_PICKLIST_MESSAGE_TEXT.md) | `SN_PICKLIST_MESSAGE_TEXT_ID` |
| `SN_PICKLIST_MESSAGE_ID` | [SN_PICKLIST_MESSAGE](SN_PICKLIST_MESSAGE.md) | `SN_PICKLIST_MESSAGE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SN_PICKLIST_MESSAGE_TEXT](SN_PICKLIST_MESSAGE_TEXT.md) | `PARENT_MESSAGE_TEXT_ID` |

