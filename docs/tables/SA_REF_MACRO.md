# SA_REF_MACRO

> Parent record for all macros for the anesthesia applications, contains info about macro, details of the what the macro does is contained in the SA_REF_MACRO* tables Based on the # of Macros they want to build and how they want to build them (at facility/user/procedure level). As small as 5 or 6 - as large as ???? . 100

**Description:** SA Reference Macros  
**Table type:** REFERENCE  
**Primary key:** `SA_REF_MACRO_ID`  
**Columns:** 20  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `LOCATION_CD` | DOUBLE | NOT NULL |  | Defines the only location that the macro can be executed from, any location if 0 |
| 6 | `MACRO_NAME` | VARCHAR(50) | NOT NULL |  | The display name of the macro |
| 7 | `MACRO_NAME_KEY` | VARCHAR(50) |  |  | Macro Name Key. All Caps with no spaces. |
| 8 | `MACRO_NAME_KEY_A_NLS` | VARCHAR(200) |  |  | MACRO_NAME_KEY_A_NLS column |
| 9 | `MACRO_NAME_KEY_NLS` | VARCHAR(102) |  |  | Macro Name Key NLS component |
| 10 | `ORDER_CATALOG_CD` | DOUBLE | NOT NULL |  | Defines the only procedure for the surgical_case that the macro can be executed for, any procedure if 0 |
| 11 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Defines the only user that can execute the macro, any user if 0 |
| 12 | `REF_TYPE_FLAG` | DOUBLE | NOT NULL |  | The type of reference this item is built for (I.e Anesthesia (0), CVNet (1) |
| 13 | `SA_REF_CATEGORY_ID` | DOUBLE | NOT NULL | FK→ | Id to the SA category that the macro belongs to |
| 14 | `SA_REF_DOC_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Doc Type that Macro is available for. |
| 15 | `SA_REF_MACRO_ID` | DOUBLE | NOT NULL | PK | Unique value that identifies each macro |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SA_REF_CATEGORY_ID` | [SA_REF_CATEGORY](SA_REF_CATEGORY.md) | `SA_REF_CATEGORY_ID` |
| `SA_REF_DOC_TYPE_ID` | [SA_REF_DOC_TYPE](SA_REF_DOC_TYPE.md) | `SA_REF_DOC_TYPE_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [SA_MACRO](SA_MACRO.md) | `SA_REF_MACRO_ID` |
| [SA_REF_MACRO_ACTION](SA_REF_MACRO_ACTION.md) | `SA_REF_MACRO_ID` |
| [SA_REF_MACRO_FLUID](SA_REF_MACRO_FLUID.md) | `SA_REF_MACRO_ID` |
| [SA_REF_MACRO_ITEM](SA_REF_MACRO_ITEM.md) | `SA_REF_MACRO_ID` |
| [SA_REF_MACRO_MEDICATION](SA_REF_MACRO_MEDICATION.md) | `SA_REF_MACRO_ID` |
| [SA_REF_MACRO_PARAMETER](SA_REF_MACRO_PARAMETER.md) | `SA_REF_MACRO_ID` |
| [SA_REF_MACRO_SEQUENCE](SA_REF_MACRO_SEQUENCE.md) | `SA_REF_MACRO_ID` |

