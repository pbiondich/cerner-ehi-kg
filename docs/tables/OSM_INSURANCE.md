# OSM_INSURANCE

> OSM Insurance.

**Description:** This table contains OSM insurance information.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 16

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ADDITIONAL_INFO` | VARCHAR(30) |  |  | This is the free text field to store the additional information of OSM insurance. |
| 2 | `ENCOUNTER_ID` | DOUBLE | NOT NULL |  | This is the foreign key to the Encounter table. |
| 3 | `FINANCIAL_CLASS` | VARCHAR(30) |  |  | This is string that contains financial class. |
| 4 | `GROUP_NAME` | VARCHAR(30) |  |  | This is the insurance group name. |
| 5 | `GROUP_NBR` | VARCHAR(15) |  |  | This is the insurance group number. |
| 6 | `HEALTH_PLAN` | VARCHAR(30) |  |  | This is the health plan name. |
| 7 | `INSURANCE_COMPANY` | VARCHAR(30) |  |  | This is the insurance company name. |
| 8 | `MEMBER_NBR` | VARCHAR(15) |  |  | This is the insurance membership number. |
| 9 | `POLICY_NBR` | VARCHAR(15) |  |  | This is the Policy Number. |
| 10 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | This is the insurance priority sequence, such as primary, and secondary. |
| 11 | `SPONSOR_ID` | DOUBLE | NOT NULL | FK→ | This field contains the identifier of the organization that is sponsoring the health plan. |
| 12 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 13 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 14 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 15 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 16 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SPONSOR_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |

