# SN_PICKLIST_MESSAGE

> Contains message information for surgical picklist and picklist items

**Description:** Surginet Picklist Message  
**Table type:** ACTIVITY  
**Primary key:** `SN_PICKLIST_MESSAGE_ID`  
**Columns:** 12  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MESSAGE_TYPE_CD` | DOUBLE | NOT NULL |  | A code indicating the Type of message |
| 2 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Contains the primary key to the parent table identified in field PARENT_ENTITY_NAME |
| 3 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Contains the table name of the parent |
| 4 | `RESOLVED_DT_TM` | DATETIME |  |  | Indicates the date when the message was resolved |
| 5 | `RESOLVED_IND` | DOUBLE | NOT NULL |  | Indicates whether or not the message has been resolved |
| 6 | `RESOLVED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel id of the user who resolved the message |
| 7 | `SN_PICKLIST_MESSAGE_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `RESOLVED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SN_PICKLIST_MESSAGE_TEXT](SN_PICKLIST_MESSAGE_TEXT.md) | `SN_PICKLIST_MESSAGE_ID` |

