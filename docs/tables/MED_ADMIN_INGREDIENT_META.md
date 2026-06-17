# MED_ADMIN_INGREDIENT_META

> Table containing medication ingredient metadata related to medication administration records.

**Description:** Medication Administration Ingredient Metadata  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADMIN_BLOB` | LONGBLOB |  |  | A BLOB containing the JSON representation of medication administration records. |
| 2 | `BLOB_DEF_VERSION` | DOUBLE | NOT NULL |  | Version of the data definition contained in the ADMINS_BLOB. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the ENCOUNTER table. |
| 4 | `INGREDIENT_REF_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the ORDER_CATALOG table. |
| 5 | `MED_ADMIN_INGREDIENT_META_ID` | DOUBLE | NOT NULL |  | PRIMARY KEY |
| 6 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Unique generated number that identifies a single row on the PERSON table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `INGREDIENT_REF_ID` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

