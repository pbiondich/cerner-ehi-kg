# PERSON_TRANSPLANT_CANDIDATE

> Identifies a person as a candidate for transplantation and defines their need and other relevant information.

**Description:** Person Transplant Candidate  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 32

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `COMMENT_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific long_text record where Transplant Candidate comments are stored. It is a foreign key reference to the primary key of the long_text table. |
| 6 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 7 | `CRITICALITY_CD` | DOUBLE | NOT NULL |  | The code for the recipient criticality. |
| 8 | `CURRENT_DRUG_THERAPY` | VARCHAR(255) |  |  | Text describing the current drug therapy for the person. |
| 9 | `DIAGNOSIS` | VARCHAR(255) |  |  | Text describing the transplant candidiates diagnosis. |
| 10 | `DIALYSIS_CLINIC_CD` | DOUBLE | NOT NULL |  | The code value to the Dialysis Clinic for the organ |
| 11 | `HIC_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | HIC Alias ID. Additional field for alias capture (alias person type) |
| 12 | `NMDP_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | Relates this record to a specific person_alias record where the NMDP id is stored. It is a foreign key reference to the primary key of the person_alias table. |
| 13 | `NMDP_ASSIGNED_IND` | DOUBLE |  |  | Indicates that the donor has been assigned an id from the National Marrow Donor Program. |
| 14 | `OPO_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | OPO Alias ID. Additional field for alias capture (alias person type) |
| 15 | `ORGAN_SIZE` | DOUBLE |  |  | The size of the organ to be donated (if applicable). |
| 16 | `ORGAN_TYPE_CD` | DOUBLE | NOT NULL |  | The code for the type of organ needed. |
| 17 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 18 | `PERSON_TRANSPLANT_ID` | DOUBLE | NOT NULL |  | A sequentially assigned number which uniquely identifies a Transplant Candidate record. |
| 19 | `PREV_TRANSPLANT_DT_TM` | DATETIME |  |  | Date and time of the most recent previous transplant (if any). |
| 20 | `PREV_TRANSPLANT_IND` | DOUBLE |  |  | Indicates that the person has previously been transplaneted with this type of organ. |
| 21 | `PRIORITY_CD` | DOUBLE | NOT NULL |  | The code for the tranplant priority. |
| 22 | `PX_ALIAS_ID` | DOUBLE | NOT NULL | FK→ | PX Alias ID. Additional field for alias capture (alias person type) |
| 23 | `TRANSPLANT_CENTER_CD` | DOUBLE | NOT NULL |  | The code value to the Transplant Center for the organ. |
| 24 | `TRANSPLANT_DT_TM` | DATETIME |  |  | Date and time the transplant this record refers to took place. |
| 25 | `TRANSPLANT_IND` | DOUBLE |  |  | Indicates that the transplant this record refers to has taken place. |
| 26 | `UNOS_ALIAS_ID` | DOUBLE | NOT NULL |  | Relates this record to a specific person_alias record where the UNOS id is stored. It is a foreign key reference to the primary key of the person_alias table. |
| 27 | `UNOS_ASSIGNED_IND` | DOUBLE |  |  | Indicates that the donor has been assigned an id from the United Network of Organ Sharing. |
| 28 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 29 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 30 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 31 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 32 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `COMMENT_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `HIC_ALIAS_ID` | [PERSON_ALIAS](PERSON_ALIAS.md) | `PERSON_ALIAS_ID` |
| `NMDP_ALIAS_ID` | [PERSON_ALIAS](PERSON_ALIAS.md) | `PERSON_ALIAS_ID` |
| `OPO_ALIAS_ID` | [PERSON_ALIAS](PERSON_ALIAS.md) | `PERSON_ALIAS_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PX_ALIAS_ID` | [PERSON_ALIAS](PERSON_ALIAS.md) | `PERSON_ALIAS_ID` |

