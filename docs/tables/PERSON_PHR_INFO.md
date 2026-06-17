# PERSON_PHR_INFO

> The person personal health record information table contains information specific to a patient's personal health record enrollment.

**Description:** Person Personal Health Record Information  
**Table type:** ACTIVITY  
**Primary key:** `PERSON_PHR_INFO_ID`  
**Columns:** 10  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 3 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 4 | `PERSON_PHR_INFO_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the person personal health record information table. It is an internally assigned number and generally not revealed to the user. |
| 5 | `PHR_STATUS_CD` | DOUBLE | NOT NULL |  | Code value indicating the status of the patient's personal health record election (i.e. YES, NO) |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [PERSON_PHR_INFO_HIST](PERSON_PHR_INFO_HIST.md) | `PERSON_PHR_INFO_ID` |
| [PERSON_PHR_RELTN](PERSON_PHR_RELTN.md) | `PERSON_PHR_INFO_ID` |
| [PERSON_PHR_RELTN_HIST](PERSON_PHR_RELTN_HIST.md) | `PERSON_PHR_INFO_ID` |

