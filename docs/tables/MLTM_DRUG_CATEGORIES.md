# MLTM_DRUG_CATEGORIES

> This table assigns a textual description to each therapeutic/chemical drug category identification number.

**Description:** This table assigns a textual description to each therapeutic/chemical drug cat.  
**Table type:** REFERENCE  
**Primary key:** `MULTUM_CATEGORY_ID`  
**Columns:** 8  
**Referenced by:** 6 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATEGORY_ATC_CODE` | VARCHAR(20) | NOT NULL |  | The code which denotes the appropriate alternative therapeutic class. |
| 2 | `CATEGORY_NAME` | VARCHAR(255) |  |  | This field contains a textual description of the therapeutic/chemical category referenced by Multum_category_id. |
| 3 | `MULTUM_CATEGORY_ID` | DOUBLE | NOT NULL | PK | This field is used to assign a therapeutic/chemical category to a specific drug. |
| 4 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 5 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 6 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 7 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 8 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (6)

| From table | Column |
|------------|--------|
| [CMS_CRITICAL_CATEGORY](CMS_CRITICAL_CATEGORY.md) | `MULTUM_CATEGORY_ID` |
| [MLTM_ALT_DRUG_CAT_NAME](MLTM_ALT_DRUG_CAT_NAME.md) | `CATEGORY_ID` |
| [MLTM_CATEGORY_DRUG_XREF](MLTM_CATEGORY_DRUG_XREF.md) | `MULTUM_CATEGORY_ID` |
| [MLTM_CATEGORY_SUB_XREF](MLTM_CATEGORY_SUB_XREF.md) | `MULTUM_CATEGORY_ID` |
| [MLTM_CATEGORY_SUB_XREF](MLTM_CATEGORY_SUB_XREF.md) | `SUB_CATEGORY_ID` |
| [MLTM_DDM_GROUP_MMDC_MAP](MLTM_DDM_GROUP_MMDC_MAP.md) | `MULTUM_CATEGORY_ID` |

