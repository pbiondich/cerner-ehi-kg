# HF_D_COLLECTION_SRC_SITE

> health facts dimension collection source site table

**Description:** HF_D_COLLECTION_SRC_SITE  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COLLECTION_SOURCE_SITE_DESC` | VARCHAR(40) |  |  | The collection source or site for the microbiology specimen |
| 2 | `COLLECTION_SOURCE_SITE_ID` | DOUBLE |  |  | Primary key to the table. Uniquely defines a collection source/site |
| 3 | `HL7_CODE` | VARCHAR(6) |  |  | The SNOMED code for sources from an HL7 file |
| 4 | `METHOD_SNOMED` | VARCHAR(10) |  |  | If this record is a collection method, this is the collection method SNOMED CT code. |
| 5 | `MODIFIER_DESC` | VARCHAR(100) |  |  | If the source/site has a modifier such as left, right, upper, lower, this field is the modifier description like Left, Right. |
| 6 | `MODIFIER_SNOMED` | VARCHAR(10) |  |  | If the source/site has a modifier such as left, right, upper, lower, this field is the SNOMED for the modifier. |
| 7 | `SITE_IND` | DOUBLE |  |  | An indicator to flag the items most commonly considered a specimen site |
| 8 | `SITE_SNOMED` | VARCHAR(10) |  |  | If this record is a body site, this is the site SNOMED CT code. |
| 9 | `SNOMED_CODE` | VARCHAR(10) |  |  | The SNOMED 5 code for a specimen source |
| 10 | `SOURCE_IND` | DOUBLE |  |  | An indicator to flag the items most commonly considered a specimen source |
| 11 | `SOURCE_TYPE` | VARCHAR(20) |  |  | A grouping for common sources |
| 12 | `STERILE_IND` | DOUBLE |  |  | An indicator to flag the sources/sites considered sterile |
| 13 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 15 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

