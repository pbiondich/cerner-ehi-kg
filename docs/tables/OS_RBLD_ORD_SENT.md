# OS_RBLD_ORD_SENT

> OS_RBLD_ORD_SENT is used to store existing and rebuilt data from the ORDER_SENTENCE table.

**Description:** OS_RBLD_ORD_SENT  
**Table type:** ACTIVITY  
**Primary key:** `OS_RBLD_ORD_SENT_ID`  
**Columns:** 51  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMMITTED_FLAG` | DOUBLE | NOT NULL |  | Used to indicate the processing status of the rebuilt order sentence. 0 - Not processed, 1 - No update needed, 2 - Errors when updating, 3 - Committed, 4 - Errors on rollback, 5 - Rolled back. |
| 2 | `EXTERNAL_IDENTIFIER_IND` | DOUBLE | NOT NULL |  | Indicates the value for column EXTERNAL_IDENTIFIER on the order_sentence table was NULL. Null values do not come through the message buss. They get changed to a 0 or blank. Used when identifying the appropriate row to be removed when updating order sentence values. |
| 3 | `NEW_DISCERN_AUTO_VERIFY_FLAG` | DOUBLE | NOT NULL |  | Rebuilt discern_auto_verify_flag |
| 4 | `NEW_EXTERNAL_IDENTIFIER` | VARCHAR(50) | NOT NULL |  | Rebuilt external_identifier |
| 5 | `NEW_IC_AUTO_VERIFY_FLAG` | DOUBLE | NOT NULL |  | Rebuilt ic_auto_verify_flag |
| 6 | `NEW_OE_FORMAT_ID` | DOUBLE | NOT NULL |  | Rebuilt oe_format_id |
| 7 | `NEW_ORDER_ENCNTR_GROUP_CD` | DOUBLE | NOT NULL |  | Rebuilt order_encounter_group_cd |
| 8 | `NEW_ORD_COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Rebuilt ord_comment_long_text_id |
| 9 | `NEW_ORD_SENT_DISP_LINE` | VARCHAR(255) | NOT NULL |  | Rebuilt ord_sent_disp_line |
| 10 | `NEW_PARENT_ENTITY2_ID` | DOUBLE | NOT NULL |  | Rebuilt parent_entity2_id |
| 11 | `NEW_PARENT_ENTITY2_NAME` | VARCHAR(30) | NOT NULL |  | Rebuilt parent_entity2_name |
| 12 | `NEW_PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Rebuilt parent_entity_id |
| 13 | `NEW_PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Rebuilt parent_entity_name |
| 14 | `NEW_RX_TYPE_MEAN` | VARCHAR(12) | NOT NULL |  | Rebuilt rx_type_mean |
| 15 | `NEW_UPDT_APPLCTX` | DOUBLE | NOT NULL |  | Rebuilt updt_applctx |
| 16 | `NEW_UPDT_CNT` | DOUBLE | NOT NULL |  | Rebuilt updt_cnt |
| 17 | `NEW_UPDT_DT_TM` | DATETIME | NOT NULL |  | Rebuilt updt_dt_tm |
| 18 | `NEW_UPDT_ID` | DOUBLE | NOT NULL |  | Rebuilt updt_id |
| 19 | `NEW_UPDT_TASK` | DOUBLE | NOT NULL |  | Rebuilt updt_task |
| 20 | `NEW_USAGE_FLAG` | DOUBLE | NOT NULL |  | Rebuilt usage_flag |
| 21 | `OLD_DISCERN_AUTO_VERIFY_FLAG` | DOUBLE | NOT NULL |  | Existing discern_auto_verify_flag value on the order_sentence table |
| 22 | `OLD_EXTERNAL_IDENTIFIER` | VARCHAR(50) | NOT NULL |  | Existing external_identifier value on the order_sentence table |
| 23 | `OLD_IC_AUTO_VERIFY_FLAG` | DOUBLE | NOT NULL |  | Existing ic_auto_verify_flag value on the order_sentence table |
| 24 | `OLD_OE_FORMAT_ID` | DOUBLE | NOT NULL |  | Existing oe_format_id value on the order_sentence table |
| 25 | `OLD_ORDER_ENCNTR_GROUP_CD` | DOUBLE | NOT NULL |  | Existing order_encntr_group_cd value on the order_sentence table |
| 26 | `OLD_ORD_COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | Existing ord_comment_long_text_id value on the order_sentence table |
| 27 | `OLD_ORD_SENT_DISP_LINE` | VARCHAR(255) | NOT NULL |  | Existing ord_sent_disp_line on the order_sentence table |
| 28 | `OLD_PARENT_ENTITY2_ID` | DOUBLE | NOT NULL |  | Existing parent_entity2_id value on the order_sentence table |
| 29 | `OLD_PARENT_ENTITY2_NAME` | VARCHAR(30) | NOT NULL |  | Existing parent_entity2_name value on the order_sentence table |
| 30 | `OLD_PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Existing parent_entity_id value on the order_sentence table |
| 31 | `OLD_PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | Existing parent_entity_name value on the order_sentence table |
| 32 | `OLD_RX_TYPE_MEAN` | VARCHAR(12) | NOT NULL |  | Existing rx_type_mean value on the order_sentence table |
| 33 | `OLD_UPDT_APPLCTX` | DOUBLE | NOT NULL |  | Existing updt_applctx value on the order_sentence table |
| 34 | `OLD_UPDT_CNT` | DOUBLE | NOT NULL |  | Existing updt_cnt value on the order_sentence table |
| 35 | `OLD_UPDT_DT_TM` | DATETIME | NOT NULL |  | Existing updt_dt_tm value on the order_sentence table |
| 36 | `OLD_UPDT_ID` | DOUBLE | NOT NULL |  | Existing updt_id value on the order_sentence table |
| 37 | `OLD_UPDT_TASK` | DOUBLE | NOT NULL |  | Existing updt_task value on the order_sentence table |
| 38 | `OLD_USAGE_FLAG` | DOUBLE | NOT NULL |  | Existing usage_flag value on the order_sentence table |
| 39 | `ORDER_SENTENCE_ID` | DOUBLE | NOT NULL |  | The corresponding order_sentence_id on the order_sentence table. |
| 40 | `ORD_SENT_DISP_LINE_IND` | DOUBLE | NOT NULL |  | Indicates the value for column ORDER_SENTENCE_DISPLAY_LINE on the order_sentence table was NULL. Null values do not come through the message buss. They get changed to a 0 or blank. Used when identifying the appropriate row to be removed when updating order sentence values. |
| 41 | `OS_RBLD_ORD_SENT_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the OS_RBLD_ORD_SENT table. |
| 42 | `PARENT_ENTITY2_NAME_IND` | DOUBLE | NOT NULL |  | Indicates the value for column PARENT_ENTITY2_NAME on the order_sentence table was NULL. Null values do not come through the message buss. They get changed to a 0 or blank. Used when identifying the appropriate row to be removed when updating order sentence values. |
| 43 | `PARENT_SYNONYM_TEXT` | VARCHAR(100) | NOT NULL |  | The synonym mnemonic of the order sentence. |
| 44 | `PRSNL_ID` | DOUBLE | NOT NULL |  | The prsnl_id of the person that executed the rebuild utility. |
| 45 | `RUN_DT_TM` | DATETIME | NOT NULL |  | The date/time the rebuild utility was run. |
| 46 | `RX_TYPE_MEAN_IND` | DOUBLE | NOT NULL |  | Indicates the value for column RX_TYPE_MEAN on the order_sentence table was NULL. Null values do not come through the message buss. They get changed to a 0 or blank. Used when identifying the appropriate row to be removed when updating order sentence values. |
| 47 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 49 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 50 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 51 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (2)

| From table | Column |
|------------|--------|
| [OS_RBLD_MSG](OS_RBLD_MSG.md) | `OS_RBLD_ORD_SENT_ID` |
| [OS_RBLD_ORD_SENT_DET](OS_RBLD_ORD_SENT_DET.md) | `OS_RBLD_ORD_SENT_ID` |

