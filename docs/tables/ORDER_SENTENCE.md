# ORDER_SENTENCE

> Order sentence is used to default order detail values when user places order. Order_sentence table stores order sentences and their detail display lines.

**Description:** Order Sentence  
**Table type:** REFERENCE  
**Primary key:** `ORDER_SENTENCE_ID`  
**Columns:** 19  
**Referenced by:** 12 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DISCERN_AUTO_VERIFY_FLAG` | DOUBLE | NOT NULL |  | Flag representing current order catalog's auto verification settings for Discern Alerts. '0' = No Setting '1' = "No" - No auto verification performed. '2' = "No w/Clinical Checking" - If alerts exist, auto verification is not performed. '3' = "Yes w/Reason" - Only auto verify if a reason was provided with the alert(s).'4' = "Yes" - Auto verify regardless of alerts. |
| 2 | `EXTERNAL_IDENTIFIER` | VARCHAR(50) |  |  | External identifier defined by source creating order sentence (i.e., Multum). This value uniquely identifies a record when compared against the source. |
| 3 | `IC_AUTO_VERIFY_FLAG` | DOUBLE | NOT NULL |  | Flag representing current order catalog's auto verification settings for Interaction Checking. '0' = No Setting '1' = "No" - No auto verification performed. '2' = "No w/Clinical Checking" - If alerts exist, auto verification is not performed. '3' = "Yes w/Reason" - Only auto verify if a reason was provided with the alert(s).'4' = "Yes" - Auto verify regardless of alerts. |
| 4 | `OE_FORMAT_ID` | DOUBLE | NOT NULL | FK→ | Used to trace which order entry format was used to build the order sentence |
| 5 | `ORDER_ENCNTR_GROUP_CD` | DOUBLE | NOT NULL |  | Used to associate order sentence with specific order encounter group. |
| 6 | `ORDER_SENTENCE_DISPLAY_LINE` | VARCHAR(255) |  |  | Order detail display line for the order sentence |
| 7 | `ORDER_SENTENCE_ID` | DOUBLE | NOT NULL | PK | Primary identifier column |
| 8 | `ORD_COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL |  | The order sentence comment of the order sentence. |
| 9 | `PARENT_ENTITY2_ID` | DOUBLE | NOT NULL |  | The unique identifier from the corresponding table name referenced in PARENT_ENTITY2_NAME for whichhe order sentence is stored. |
| 10 | `PARENT_ENTITY2_NAME` | VARCHAR(30) |  |  | The name of the reference table this order sentence is associated with. For example, ord_cat_sent_r, cs_component, etc. |
| 11 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | The unique identifier from the corresponding table name referenced in PARENT_ENTITY_NAME for which the order sentence is stored. |
| 12 | `PARENT_ENTITY_NAME` | VARCHAR(30) | NOT NULL |  | The name of the reference table this order sentence is associated with. For example, ord_cat_sent_r, cs_component, etc. |
| 13 | `RX_TYPE_MEAN` | VARCHAR(12) |  |  | Pharmacy type of the order sentence. Values include: MED, DILUENT, ADDITIVE, SLIDINGSCALE |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `USAGE_FLAG` | DOUBLE | NOT NULL |  | Usage Flag |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OE_FORMAT_ID` | [ORDER_ENTRY_FORMAT_PARENT](ORDER_ENTRY_FORMAT_PARENT.md) | `OE_FORMAT_ID` |

## Referenced by (12)

| From table | Column |
|------------|--------|
| [ACT_PW_COMP](ACT_PW_COMP.md) | `ORDER_SENTENCE_ID` |
| [ALT_SEL_LIST](ALT_SEL_LIST.md) | `ORDER_SENTENCE_ID` |
| [CS_COMPONENT](CS_COMPONENT.md) | `ORDER_SENTENCE_ID` |
| [MRU_LOOKUP_ORDER](MRU_LOOKUP_ORDER.md) | `ORDER_SENTENCE_ID` |
| [ORDER_SENTENCE_DETAIL](ORDER_SENTENCE_DETAIL.md) | `ORDER_SENTENCE_ID` |
| [ORDER_SENTENCE_FILTER](ORDER_SENTENCE_FILTER.md) | `ORDER_SENTENCE_ID` |
| [PATHWAY_COMP](PATHWAY_COMP.md) | `ORDER_SENTENCE_ID` |
| [PW_COMP_OS_RELTN](PW_COMP_OS_RELTN.md) | `ORDER_SENTENCE_ID` |
| [RX_AUTO_VERIFY_ING_AUDIT](RX_AUTO_VERIFY_ING_AUDIT.md) | `ORDER_SENTENCE_ID` |
| [RX_THERAP_SBSTTN_TO](RX_THERAP_SBSTTN_TO.md) | `TO_ORDER_SENTENCE_ID` |
| [SCH_APPT_SYN](SCH_APPT_SYN.md) | `ORDER_SENTENCE_ID` |
| [SCH_EVENT](SCH_EVENT.md) | `ORDER_SENTENCE_ID` |

