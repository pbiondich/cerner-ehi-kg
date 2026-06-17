# PW_COMP_OS_RELTN

> Used to define relationships between a pathway component and order sentences.

**Description:** Pathway component order sentence relationship.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `IV_COMP_SYN_ID` | DOUBLE | NOT NULL |  | IV Component Synonym ID. Represents the synonym-id of the COMP_ID field from the CS_COMPONENT table. This is not a FK because COMP_ID is not a PK field it that table. |
| 2 | `MISSING_REQUIRED_IND` | DOUBLE | NOT NULL |  | Indicates whether the order sentence in the OS_DISPLAY_LINE column on the table has all the reuired fields populated based on the component format. |
| 3 | `NORMALIZED_DOSE_UNIT_IND` | DOUBLE | NOT NULL |  | Indicates whether the order sentence contains a strength dose unit or volume dose unit that is a normalized unit as defined within the code-value extension (field value bitmask includes a value of 32) of CodeSet 54. Examples of normalized dose units are weight-based, mg/kg, or body surface area (BSA)-based, mg/m2. |
| 4 | `ORDER_SENTENCE_ID` | DOUBLE | NOT NULL | FK→ | Order sentence id from the order_sentence table. |
| 5 | `ORDER_SENTENCE_SEQ` | DOUBLE |  |  | Sequence of the order sentence for the component. |
| 6 | `OS_DISPLAY_LINE` | VARCHAR(255) |  |  | Order Sentence Display LineColumn |
| 7 | `PATHWAY_COMP_ID` | DOUBLE | NOT NULL | FK→ | Pathway component id from the pathway_comp table. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_SENTENCE_ID` | [ORDER_SENTENCE](ORDER_SENTENCE.md) | `ORDER_SENTENCE_ID` |
| `PATHWAY_COMP_ID` | [PATHWAY_COMP](PATHWAY_COMP.md) | `PATHWAY_COMP_ID` |

