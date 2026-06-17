# LOGIN_TEMPLATE

> Stores all of the login templates. Login Templates control the behavior of the PathNet Collections: Specimen Login application.

**Description:** Login Template  
**Table type:** REFERENCE  
**Primary key:** `TEMPLATE_CD`  
**Columns:** 9  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFAULT_IND` | DOUBLE |  |  | This field determines which login template will be used as the default template for users to whom another template is not assigned. Only one row on this table should have this field set to 1 (default). All other rows should have this field set to 0. |
| 2 | `TEMPLATE_CD` | DOUBLE | NOT NULL | PK | Code value associated with the login template described by this row. |
| 3 | `TEMPLATE_NAME` | VARCHAR(50) | NOT NULL |  | Textual name of the login template defined by this row. |
| 4 | `TEMPLATE_TYPE_FLAG` | DOUBLE | NOT NULL |  | Determines the type of login template. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (1)

| From table | Column |
|------------|--------|
| [LOGIN_TEMPLATE_PREFERENCE](LOGIN_TEMPLATE_PREFERENCE.md) | `TEMPLATE_CD` |

