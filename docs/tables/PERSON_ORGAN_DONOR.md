# PERSON_ORGAN_DONOR

> Identifies a person as an organ donor and defines the type of organ, the conditions for donation and other relevant information.

**Description:** Person Organ Donor  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific long_text record where Organ Donor comments are stored. It is a foreign key reference to the primary key of the long_text table. |
| 6 | `CURRENT_DRUG_THERAPY` | VARCHAR(255) |  |  | Text describing the current drug therapy for the person. |
| 7 | `DONATION_DT_TM` | DATETIME |  |  | Date and time that the organ was donated. |
| 8 | `DONATION_IND` | DOUBLE |  |  | Indicates that the organ has been donated. |
| 9 | `DONOR_TYPE_CD` | DOUBLE | NOT NULL |  | The code for the type of organ donation. Specifies when the organ is or will be available (e.g. living donation, upon death, or deceased and available). |
| 10 | `INTL_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | International Alias ID. Additional fields for alias capture (alias person type). |
| 11 | `NMDP_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific person_alias record where the NMDP id is stored. It is a foreign key reference to the primary key of the person_alias table. |
| 12 | `NMDP_ASSIGNED_IND` | DOUBLE |  |  | Indicates that the donor has been assigned an id from the National Marrow Donor Program. |
| 13 | `OPO_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | OPO Alias ID. Additional fields for alias capture (alias person type). |
| 14 | `ORGAN_SIZE` | DOUBLE |  |  | The size of the organ to be donated (if applicable). |
| 15 | `ORGAN_TYPE_CD` | DOUBLE | NOT NULL |  | The code for the type of organ to be donated. |
| 16 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 17 | `PERSON_ORGAN_ID` | DOUBLE | NOT NULL |  | A sequentially assigned number which uniquely identifies an Organ Donor record. |
| 18 | `UNOS_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific person_alias record where the UNOS id is stored. It is a foreign key reference to the primary key of the person_alias table. |
| 19 | `UNOS_ASSIGNED_IND` | DOUBLE |  |  | Indicates that the donor has been assigned an id from the United Network of Organ Sharing. |
| 20 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 21 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 22 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 23 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 24 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `INTL_ALIAS_ID` | [PERSON_ALIAS](PERSON_ALIAS.md) | `PERSON_ALIAS_ID` |
| `NMDP_ALIAS_ID` | [PERSON_ALIAS](PERSON_ALIAS.md) | `PERSON_ALIAS_ID` |
| `OPO_ALIAS_ID` | [PERSON_ALIAS](PERSON_ALIAS.md) | `PERSON_ALIAS_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `UNOS_ALIAS_ID` | [PERSON_ALIAS](PERSON_ALIAS.md) | `PERSON_ALIAS_ID` |

