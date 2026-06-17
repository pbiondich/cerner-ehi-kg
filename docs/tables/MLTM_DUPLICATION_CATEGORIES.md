# MLTM_DUPLICATION_CATEGORIES

> Therapeutic duplication category, as well as certain descriptive information: a display name for each therapeutic duplication category and a number representing the allowable number of active prescriptions or orders for drugs within a particular category.

**Description:** Multum Duplication Categories  
**Table type:** REFERENCE  
**Primary key:** `MULTUM_CATEGORY_ID`  
**Columns:** 8  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATEGORY_NAME` | VARCHAR(100) |  |  | Contains a textual description of the therapeutic duplication category referenced by Multum_category_id. |
| 2 | `MAX_THERAPEUTIC_DUPLICATION` | DOUBLE |  |  | How many drugs in a specified category may be prescribed before therapeutic duplication warnings should be generated. |
| 3 | `MULTUM_CATEGORY_ID` | DOUBLE | NOT NULL | PK | The therapeutic duplication category to a specific drug. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (3)

| From table | Column |
|------------|--------|
| [MLTM_DUPLICATION_DRUG_XREF](MLTM_DUPLICATION_DRUG_XREF.md) | `MULTUM_CATEGORY_ID` |
| [MLTM_DUPLICATION_SUB_XREF](MLTM_DUPLICATION_SUB_XREF.md) | `MULTUM_CATEGORY_ID` |
| [MLTM_DUPLICATION_SUB_XREF](MLTM_DUPLICATION_SUB_XREF.md) | `SUB_CATEGORY_ID` |

