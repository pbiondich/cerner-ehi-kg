# HE_SESSION_CONSEQUENT

> Keeping the current state of health expert session consequents.

**Description:** Health Expert Session Consequents  
**Table type:** ACTIVITY  
**Primary key:** `SESSION_CONSEQUENT_ID`  
**Columns:** 17  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `CERTAINTY` | DOUBLE | NOT NULL |  | The certainty of this consequent. This will range from -100 to +100. |
| 4 | `CONSEQUENT_NAME` | VARCHAR(100) | NOT NULL |  | The name of the consequent. |
| 5 | `CONSEQUENT_VALUE_TXT` | VARCHAR(255) | NOT NULL |  | The value of the consequent. |
| 6 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 7 | `EXPLANATION` | VARCHAR(255) | NOT NULL |  | The explanation of why this consequent was inferred. |
| 8 | `KNOWLEDGEBASE_NAME` | VARCHAR(100) |  |  | The name of the Knowledgebase |
| 9 | `SERIALIZED_CLASS` | VARCHAR(500) |  |  | Class path of the SERIALIZED_OBJECT |
| 10 | `SERIALIZED_OBJECT` | VARCHAR(4000) |  |  | JSON representation of the consequent containing data outside the scope of a Simple Consequent |
| 11 | `SESSION_CONSEQUENT_ID` | DOUBLE | NOT NULL | PK | The unique identifier for each session consequent row. |
| 12 | `SESSION_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the session this consequent is associated with. |
| 13 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 14 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 15 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 16 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 17 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SESSION_ID` | [HE_SESSION](HE_SESSION.md) | `SESSION_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [HE_CONSEQUENT_QUEUE](HE_CONSEQUENT_QUEUE.md) | `SESSION_CONSEQUENT_ID` |

