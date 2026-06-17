# ORDER_SENTENCE_DETAIL

> Order Sentence Detail

**Description:** The individual fields that make up the order sentence.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFAULT_PARENT_ENTITY_ID` | DOUBLE |  |  | The ID of the data to be used for the default value. If valued, this field should be the same as the oe_field_value for the record. |
| 2 | `DEFAULT_PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | The table name where the default (for codesets and lists) is located, for example CODE_VALUE. This field is empty for oe fields with defaults that are not codes or IDs. |
| 3 | `FIELD_TYPE_FLAG` | DOUBLE |  |  | The data type for this field. |
| 4 | `OE_FIELD_DISPLAY_VALUE` | VARCHAR(255) |  |  | The displayable value for the order detail. |
| 5 | `OE_FIELD_ID` | DOUBLE | NOT NULL | FK→ | The identifier of which order entry field this detail record is for. |
| 6 | `OE_FIELD_MEANING_ID` | DOUBLE | NOT NULL |  | Identifies what the order entry field is for (e.g. frequency, start date/time). |
| 7 | `OE_FIELD_VALUE` | DOUBLE |  |  | The numeric default value for the record. If this record is for a non-numeric or non-coded default value, this field will be zero. |
| 8 | `ORDER_SENTENCE_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the order sentence this detail record belongs to. |
| 9 | `SEQUENCE` | DOUBLE | NOT NULL |  | Sequence value |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OE_FIELD_ID` | [ORDER_ENTRY_FIELDS](ORDER_ENTRY_FIELDS.md) | `OE_FIELD_ID` |
| `ORDER_SENTENCE_ID` | [ORDER_SENTENCE](ORDER_SENTENCE.md) | `ORDER_SENTENCE_ID` |

