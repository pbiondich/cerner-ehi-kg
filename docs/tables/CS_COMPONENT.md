# CS_COMPONENT

> Stores information about every component of a CareSet or a CarePlan

**Description:** Stores the components that make up a CareSet or CarePlan.  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 27

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AV_OPTIONAL_INGREDIENT_IND` | DOUBLE |  |  | Indicates if an ingredient is optional for auto-verification consideration. 0 = Required, 1 = Optional |
| 2 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | This field contains the code from the Order Catalog table for which this entry is a component of. |
| 3 | `COMP_ID` | DOUBLE | NOT NULL | FK→ | This field contains the id for external tables for which this component has data on. (i.e. Long Text ID, Synonym_ID) |
| 4 | `COMP_LABEL` | VARCHAR(255) |  |  | The display value for the component. |
| 5 | `COMP_MASK` | DOUBLE |  |  | component mask |
| 6 | `COMP_REFERENCE` | VARCHAR(255) |  |  | Text or link to text containing information about this component. |
| 7 | `COMP_SEQ` | DOUBLE | NOT NULL |  | The sequence of the components within this CarePlan or CareSet. |
| 8 | `COMP_TYPE_CD` | DOUBLE | NOT NULL |  | This field defines what type of component it is. |
| 9 | `COMP_TYPE_MEAN` | VARCHAR(15) |  |  | A textual string defining what type of component it is. |
| 10 | `CP_COL_CAT_CD` | DOUBLE | NOT NULL |  | This field defines where in the CarePlan grid this component resides in, specifically the column category. |
| 11 | `CP_ROW_CAT_CD` | DOUBLE | NOT NULL |  | This field defines where in the CarePlan grid the component resides in, specifically the row category. |
| 12 | `INCLUDE_EXCLUDE_IND` | DOUBLE |  |  | An indicator on whether this optional component should be defaulted as included or excluded. |
| 13 | `INDEX_TYPE_CD` | DOUBLE |  |  | Defines what type of index to use for lookup. |
| 14 | `LINKED_DATE_COMP_SEQ` | DOUBLE |  |  | This field contains the sequence of another component whose start date will control the start date of this field. |
| 15 | `LOCKDOWN_DETAILS_FLAG` | DOUBLE |  |  | Determines whether the IV Ingredient's details can be altered manually by the user (not locked down)or populated via an order sentence only (locked down). |
| 16 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | This field contains the id from the Long Text table where components of type 'NOTE' information is stored. |
| 17 | `ORDER_SENTENCE_ID` | DOUBLE | NOT NULL | FK→ | The id from the Order Sentence table that contains the default order parameters for this order. |
| 18 | `ORD_COM_TEMPLATE_LONG_TEXT_ID` | DOUBLE |  | FK→ | Used to relate an order comment template to the component. |
| 19 | `OUTCOME_PAR_COMP_SEQ` | DOUBLE |  |  | This field contains the sequence number of the parent component which this outcome component is related to. |
| 20 | `PARENT_COMP_SEQ` | DOUBLE |  |  | The sequence of the parent component of this component. |
| 21 | `REQUIRED_IND` | DOUBLE |  |  | An indicator on whether or not this orderable component is required for this CareSet/CarePlan |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 27 | `VARIANCE_FORMAT_ID` | DOUBLE | NOT NULL |  | The format id for variances to a component. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `COMP_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ORDER_SENTENCE_ID` | [ORDER_SENTENCE](ORDER_SENTENCE.md) | `ORDER_SENTENCE_ID` |
| `ORD_COM_TEMPLATE_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

