# DA_ELEM_UDF_RELTN

> Defines relationships from Discern Analytics 2.0 elements to user-defined fields.

**Description:** Discern Analytics Element User Defined Fields Relation  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DA_ELEMENT_ID` | DOUBLE | NOT NULL | FK→ | Identifier of the element representing this user defined field in Discern Analytics 2.0. |
| 2 | `DA_ELEM_UDF_RELTN_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the DA_ELEM_UDF_RELTN table. |
| 3 | `FIELD_SEQ` | DOUBLE | NOT NULL |  | The sequence of this field in the list of parent fields for the element. |
| 4 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifier of the entity representing this user defined field. |
| 5 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | Name of the entity representing this user defined field. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DA_ELEMENT_ID` | [DA_ELEMENT](DA_ELEMENT.md) | `DA_ELEMENT_ID` |

