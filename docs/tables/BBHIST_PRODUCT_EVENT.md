# BBHIST_PRODUCT_EVENT

> This activity table is a smaller version of the Product_Event table, and is intended to store disposition information on products loaded in from previous systems.

**Description:** Blood Bank History Product Event  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 23

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BAG_RETURNED_IND` | DOUBLE |  |  | Indicates whether or not the empty bag was returned to the blood bank from the patient's location after it was transfused. |
| 6 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 7 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 8 | `EVENT_DT_TM` | DATETIME | NOT NULL |  | The date and time when this event occurred. |
| 9 | `EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | The type of event that occurred with the product. Pre-defined values by Cerner. Examples are: crossmatched, assigned, dispensed, etc. |
| 10 | `INTERNATIONAL_UNIT` | DOUBLE |  |  | The number of international units associated with this event. |
| 11 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 12 | `PRODUCT_EVENT_ID` | DOUBLE | NOT NULL |  | The primary key of this table. An internal system-assigned number that makes each row unique. |
| 13 | `PRODUCT_ID` | DOUBLE | NOT NULL |  | The primary key of this table. An internal system-assigned number that makes each row unique. |
| 14 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Represents the person who updated this product to its final disposition state. |
| 15 | `QTY` | DOUBLE |  |  | This column applies only to derivative products. It is the quantity of the derivative batch that was transfused. |
| 16 | `REASON_CD` | DOUBLE | NOT NULL |  | The reason this product was disposed of. |
| 17 | `TAG_RETURNED_IND` | DOUBLE |  |  | Indicates whether the tag attached to the bag dispensed was returned to the blood bank following the transfusion. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 23 | `VOLUME` | DOUBLE |  |  | The volume of the product that was actually infused into the patient. This amount may not be the entire volume that was in the bag. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

