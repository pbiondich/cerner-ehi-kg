# DD_REF_LABEL

> This table contains labels used to group related reference templates together.

**Description:** Dynamic Documentation - Reference Label  
**Table type:** REFERENCE  
**Primary key:** `DD_REF_LABEL_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DD_REF_LABEL_ID` | DOUBLE | NOT NULL | PK | Uniquely identifies a label used to group related reference templates together. |
| 2 | `DESCRIPTION_TXT` | VARCHAR(255) |  |  | Describes the label used to group related reference templates. |
| 3 | `DISPLAY_TXT` | VARCHAR(255) | NOT NULL |  | The display of the label. |
| 4 | `LABEL_TYPE_CD` | DOUBLE | NOT NULL |  | Types of labels used in documentation. |
| 5 | `SYSTEM_IND` | DOUBLE | NOT NULL |  | Indicates the system generated this label. Allows user created labels to coexist with reserved system labels. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `USER_ID` | DOUBLE | NOT NULL | FK→ | The user id is the user who created the label. An example of a label is "FAVORITE", a user may have marked multiple reference templates to display in a favorite templates list. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DD_REF_TMPLT_LBL_R](DD_REF_TMPLT_LBL_R.md) | `DD_REF_LABEL_ID` |

