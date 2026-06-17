# HF_D_MEDICATION

> This Health Facts dimension table contains standard values for Medications. Medications are stored at the NDC grain.

**Description:** HF_D_MEDICATION  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BRAND_NAME` | VARCHAR(100) |  |  | The brand or trade name for a medication. |
| 2 | `DOSE_FORM_DESCRIPTION` | VARCHAR(40) |  |  | The standard form in which the medication is administered (based on the Multum database). |
| 3 | `GENERIC_NAME` | VARCHAR(100) |  |  | The generic name for a medication. |
| 4 | `MEDICATION_ID` | DOUBLE |  |  | Primary key to the table. Uniquely defines a medication. |
| 5 | `NDC_CODE` | DOUBLE |  |  | The National Drug Classification code. The value does not contain formatting or leading 0's. |
| 6 | `OBSOLETE_DT_TM` | DATETIME |  |  | Contains the date when an NDC was retired. Not filled out for active NDC codes. |
| 7 | `PRODUCT_STRENGTH_DESCRIPTION` | VARCHAR(255) |  |  | The standard strength for a medication (based on the Multum database). |
| 8 | `ROUTE_DESCRIPTION` | VARCHAR(60) |  |  | The standard route of administration for a medication (based on the Multum database) |
| 9 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `UPDT_USER` | VARCHAR(40) |  |  | The user id that performed the update or insert on this record. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

