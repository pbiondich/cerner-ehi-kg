# OS_RBLD_ORD_SENT_DET

> OS_RBLD_ORD_SENT_DET is used to store existing and rebuilt data from the order_sentence_detail table

**Description:** OS_RBLD_ORD_SENT_DET  
**Table type:** ACTIVITY  
**Primary key:** `OS_RBLD_ORD_SENT_DET_ID`  
**Columns:** 41  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFAULT_PARENT_ENTITY_ID_IND` | DOUBLE | NOT NULL |  | Indicates the value for column DEFAULT_PARENT_ENTITY_ID on the order_sentence_det table was NULL. Null values do not come through the message buss. They get changed to a 0 or blank. Used when identifying the appropriate row to be removed when updating order sentence values. |
| 2 | `DEFAULT_PARENT_ENTITY_NAME_IND` | DOUBLE | NOT NULL |  | Indicates the value for column DEFAULT_PARENT_ENTITY_NAME on the order_sentence_det table was NULL. Null values do not come through the message buss. They get changed to a 0 or blank. Used when identifying the appropriate row to be removed when updating order sentence values. |
| 3 | `DELETE_OLD_IND` | DOUBLE | NOT NULL |  | Indicator used to flag deletion on old_ columns |
| 4 | `DETAIL_SEQUENCE` | DOUBLE | NOT NULL |  | Rebuild utility internal detail sequence number |
| 5 | `FIELD_TYPE_FLAG_IND` | DOUBLE | NOT NULL |  | Indicates the value for column FIELD_TYPE_FLAG on the order_sentence_det table was NULL. Null values do not come through the message buss. They get changed to a 0 or blank. Used when identifying the appropriate row to be removed when updating order sentence values. |
| 6 | `INSERT_NEW_IND` | DOUBLE | NOT NULL |  | Indicator used to flag insertion on new_ columns |
| 7 | `NEW_DEFAULT_PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Rebuilt default_parent_entity_id |
| 8 | `NEW_DEFAULT_PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Rebuilt default_parent_entity_name |
| 9 | `NEW_FIELD_TYPE_FLAG` | DOUBLE | NOT NULL |  | Rebuilt field_type_flag |
| 10 | `NEW_OE_FIELD_DISPLAY_VALUE` | VARCHAR(255) | NOT NULL |  | Rebuilt oe_field_display_value |
| 11 | `NEW_OE_FIELD_ID` | DOUBLE | NOT NULL |  | Rebuilt oe_field_id |
| 12 | `NEW_OE_FIELD_MEANING_ID` | DOUBLE | NOT NULL |  | Rebuilt oe_field_meaning_id |
| 13 | `NEW_OE_FIELD_VALUE` | DOUBLE | NOT NULL |  | Rebuilt oe_field_value |
| 14 | `NEW_SEQUENCE` | DOUBLE | NOT NULL |  | Rebuilt new_sequence |
| 15 | `NEW_UPDT_APPLCTX` | DOUBLE | NOT NULL |  | Rebuilt updt_applctx |
| 16 | `NEW_UPDT_CNT` | DOUBLE | NOT NULL |  | Rebuilt updt_cnt |
| 17 | `NEW_UPDT_DT_TM` | DATETIME | NOT NULL |  | Rebuilt updt_dt_tm |
| 18 | `NEW_UPDT_ID` | DOUBLE | NOT NULL |  | Rebuilt updt_id |
| 19 | `NEW_UPDT_TASK` | DOUBLE | NOT NULL |  | Rebuilt updt_task |
| 20 | `OE_FIELD_DISPLAY_VALUE_IND` | DOUBLE | NOT NULL |  | Indicates the value for column OE_FIELD_DISPLAY_VALUE on the order_sentence_det table was NULL. Null values do not come through the message buss. They get changed to a 0 or blank. Used when identifying the appropriate row to be removed when updating order sentence values. |
| 21 | `OE_FIELD_VALUE_IND` | DOUBLE | NOT NULL |  | Indicates the value for column OE_FIELD_VALUE on the order_sentence_det table was NULL. Null values do not come through the message buss. They get changed to a 0 or blank. Used when identifying the appropriate row to be removed when updating order sentence values. |
| 22 | `OLD_DEFAULT_PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Existing default_parent_entity_id value on the order_sentence_detail table |
| 23 | `OLD_DEFAULT_PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Existing default_parent_entity_name value on the order_sentence_detail table |
| 24 | `OLD_FIELD_TYPE_FLAG` | DOUBLE | NOT NULL |  | Existing field_type_flag value on the order_sentence_detail table |
| 25 | `OLD_OE_FIELD_DISPLAY_VALUE` | VARCHAR(255) | NOT NULL |  | Existing oe_field_display_value on the order_sentence_detail table |
| 26 | `OLD_OE_FIELD_ID` | DOUBLE | NOT NULL |  | Existing oe_field_id value on the order_sentence_detail table |
| 27 | `OLD_OE_FIELD_MEANING_ID` | DOUBLE | NOT NULL |  | Existing oe_field_meaning_id value on the order_sentence_detail table |
| 28 | `OLD_OE_FIELD_VALUE` | DOUBLE | NOT NULL |  | Existing oe_field_value on the order_sentence_detail table |
| 29 | `OLD_SEQUENCE` | DOUBLE | NOT NULL |  | Existing sequence value on the order_sentence_detail table |
| 30 | `OLD_UPDT_APPLCTX` | DOUBLE | NOT NULL |  | Existing updt_applctx value on the order_sentence_detail table |
| 31 | `OLD_UPDT_CNT` | DOUBLE | NOT NULL |  | Existing updt_cnt value on the order_sentence_detail table |
| 32 | `OLD_UPDT_DT_TM` | DATETIME | NOT NULL |  | Existing updt_dt_tm value on the order_sentence_detail table |
| 33 | `OLD_UPDT_ID` | DOUBLE | NOT NULL |  | Existing updt_id value on the order_sentence_detail table |
| 34 | `OLD_UPDT_TASK` | DOUBLE | NOT NULL |  | Existing updt_task value on the order_sentence_detail table |
| 35 | `OS_RBLD_ORD_SENT_DET_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the OS_RBLD_ORD_SENT_DET table. |
| 36 | `OS_RBLD_ORD_SENT_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the rebuilt order sentence this detail record belongs to. |
| 37 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 40 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 41 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OS_RBLD_ORD_SENT_ID` | [OS_RBLD_ORD_SENT](OS_RBLD_ORD_SENT.md) | `OS_RBLD_ORD_SENT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [OS_RBLD_MSG](OS_RBLD_MSG.md) | `OS_RBLD_ORD_SENT_DET_ID` |

